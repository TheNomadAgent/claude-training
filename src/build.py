#!/usr/bin/env python3
"""Builds index.html (the handout app), one self-contained deck per session,
the web app manifest and the service worker. Run from the repo root:

    python3 src/build.py
"""
import base64, hashlib, html, importlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content.sections import DOMAINS, SECTIONS
from content.glossary import GLOSSARY

BASE = "https://thenomadagent.github.io/claude-training/"
QR_JS = os.environ.get("QR_NODE_PATH", "/home/claude/work/node_modules")


def b64(path):
    with open(os.path.join(ROOT, path), "rb") as f:
        return base64.b64encode(f.read()).decode()


def inline(text):
    """Escape, then apply the small inline markup used in content files."""
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)

    def gloss(m):
        key, label = m.group(1), m.group(2)
        if key not in GLOSSARY:
            raise SystemExit("Unknown glossary key: " + key)
        label = label or GLOSSARY[key][0].lower()
        return '<span class="g" role="button" tabindex="0" aria-expanded="false" data-g="%s">%s</span>' % (key, label)

    return re.sub(r"\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]", gloss, t)


def pre(text, marks=False):
    t = html.escape(text, quote=False)
    if marks:
        t = re.sub(r"\{\{(.+?)\}\}", r"<mark>\1</mark>", t, flags=re.S)
    else:
        t = t.replace("{{", "").replace("}}", "")
    return t


def body_html(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if k == "h":
            out.append("<h2>%s</h2>" % inline(b[1]))
        elif k == "p":
            out.append("<p>%s</p>" % inline(b[1]))
        elif k == "pull":
            out.append('<p class="pull">%s</p>' % inline(b[1]))
        elif k == "note":
            out.append('<aside class="note"><b>%s</b><p>%s</p></aside>' % (inline(b[1]), inline(b[2])))
        elif k == "doc":
            out.append('<figure class="doc"><figcaption>%s</figcaption><pre>%s</pre></figure>' % (inline(b[1]), pre(b[2])))
        elif k == "prompt":
            out.append('<figure class="prompt"><figcaption><span>%s</span></figcaption><pre>%s</pre></figure>' % (inline(b[1]), pre(b[2])))
        elif k == "out":
            kind = b[3]
            has_marks = "{{" in b[2]
            extra = '<div class="mk">Highlighted text is not in the source.</div>' if has_marks else ""
            out.append('<figure class="out %s"><figcaption>%s</figcaption><pre>%s</pre>%s</figure>' % (kind, inline(b[1]), pre(b[2], True), extra))
        elif k == "defs":
            out.append('<dl class="defs">%s</dl>' % "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (inline(t), inline(d)) for t, d in b[1]))
        elif k == "steps":
            out.append('<ol class="steps">%s</ol>' % "".join("<li><b>%s</b><span>%s</span></li>" % (inline(t), inline(d)) for t, d in b[1]))
        elif k == "list":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in b[1]))
        elif k == "table":
            head = "".join("<th>%s</th>" % inline(x) for x in b[1])
            rows = "".join("<tr>%s</tr>" % "".join('<td data-l="%s">%s</td>' % (html.escape(b[1][i], quote=True), inline(c)) for i, c in enumerate(r)) for r in b[2])
            out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, rows))
        else:
            raise SystemExit("Unknown block type: " + k)
    return "\n".join(out)


def qr_svg(url):
    js = ("const Q=require('qrcode-svg');process.stdout.write(new Q({content:%s,padding:0,width:256,height:256,"
          "color:'#0A162B',background:'#ffffff',ecl:'M',join:true,container:'svg-viewbox'}).svg())" % json.dumps(url))
    env = dict(os.environ, NODE_PATH=QR_JS)
    return subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True, env=env).stdout


def esc(t):
    return html.escape(t, quote=False)


def slide_html(s, sess, logo_big):
    t = s["t"]
    notes = html.escape(s.get("notes", ""), quote=True)
    head = '<section class="slide t-%s" data-notes="%s"><div class="in">' % (t, notes)
    tail = "</div></section>"
    h = esc(s.get("h", ""))
    if t == "title":
        inner = ('<img class="mark" src="data:image/png;base64,%s" alt=""><h1>%s</h1><p class="sub">%s</p>'
                 '<div class="rule"></div><div class="by"><span>by <b>Justin VanAusdall</b></span></div>') % (logo_big, h, esc(s["sub"]))
    elif t == "big":
        inner = "<h2>%s</h2><p>%s</p>" % (h, esc(s.get("p", "")))
    elif t == "cards":
        cards = "".join('<div class="card fr"><h3>%s</h3><p>%s</p></div>' % (esc(a), esc(b)) for a, b in s["cards"])
        inner = '<h2>%s</h2><div class="grid c%d">%s</div>' % (h, s.get("cols", 3), cards)
    elif t == "list":
        rows = "".join('<li class="fr"><b>%s</b><span>%s</span></li>' % (esc(a), esc(b)) for a, b in s["items"])
        inner = '<h2>%s</h2><ul class="rows">%s</ul>' % (h, rows)
    elif t == "compare":
        inner = ('<h2>%s</h2><div class="two"><div class="pane bad"><div class="lb">%s</div><pre>%s</pre></div>'
                 '<div class="pane good fr"><div class="lb">%s</div><pre>%s</pre></div></div>') % (
                     h, esc(s["left_label"]), pre(s["left"]), esc(s["right_label"]), pre(s["right"]))
    elif t == "spot":
        inner = ('<h2>%s</h2><div class="two even" data-lit><div class="pane"><div class="lb">%s</div><pre>%s</pre></div>'
                 '<div class="pane bad"><div class="lb">%s</div><pre>%s</pre></div></div>'
                 '<div class="reveal fr"><b>%s</b>%s</div>') % (
                     h, esc(s["left_label"]), pre(s["left"]), esc(s["right_label"]), pre(s["right"], True),
                     esc(s.get("reveal_label", "Not in the source:")), esc(s["reveal"]))
    elif t == "code":
        small = " small" if s["pre"].count("\n") >= 14 else ""
        inner = '<h2>%s</h2><div class="pane ask single%s"><div class="lb">%s</div><pre>%s</pre></div>' % (h, small, esc(s["label"]), pre(s["pre"]))
    elif t == "ask":
        block = '<div class="pane"><pre>%s</pre></div>' % pre(s["pre"]) if s.get("pre") else ""
        inner = '<h2>%s</h2>%s<div class="reveal fr"><b>Answer:</b>%s</div>' % (h, block, esc(s["answer"]))
    elif t == "steps":
        items = "".join('<li class="fr"><small>%02d</small>%s</li>' % (n + 1, esc(x)) for n, x in enumerate(s["steps"]))
        inner = '<h2>%s</h2><ol class="way">%s</ol>' % (h, items)
    elif t == "quiz":
        url = "%s#/s/%d" % (BASE, sess["id"])
        inner = ('<div class="two"><div class="qr">%s</div><div><h2>%s</h2><p>Scan to open section %d of the handout on your phone, '
                 'then scroll to the questions.</p><div class="url">%s</div>'
                 '<a class="pill" href="../index.html#/s/%d">Open section %d</a></div></div>') % (
                     qr_svg(url), h, sess["id"], esc(url), sess["id"], sess["id"])
    else:
        raise SystemExit("Unknown slide type: " + t)
    return head + inner + tail


def main():
    sessions = {}
    for n in range(1, len(SECTIONS) + 1):
        try:
            sessions[n] = importlib.import_module("content.s%02d" % n).SESSION
        except ModuleNotFoundError:
            pass

    data = {
        "domains": [{"name": n, "w": w} for n, w in DOMAINS],
        "sections": [{"id": i + 1, "d": d, "title": t} for i, (d, t) in enumerate(SECTIONS)],
        "glossary": {k: list(v) for k, v in GLOSSARY.items()},
        "content": {},
    }
    data["exams"] = {}
    want = [8, 13, 7, 10, 7, 9, 6]
    seen = {}
    for n in range(1, 10):
        try:
            ex = importlib.import_module("content.exam%d" % n).EXAM
        except ModuleNotFoundError:
            continue
        qs = ex["questions"]
        got = [0] * 7
        for s_, q, opts in qs:
            if len(opts) != 4:
                raise SystemExit("exam %d: need 4 options: %s" % (n, q[:60]))
            if len(set(o for o, _ in opts)) != 4:
                raise SystemExit("exam %d: duplicate option: %s" % (n, q[:60]))
            if q in seen:
                raise SystemExit("exam %d: question repeats exam %d: %s" % (n, seen[q], q[:60]))
            seen[q] = n
            got[SECTIONS[s_ - 1][0]] += 1
        if len(qs) == 60 and got != want:
            raise SystemExit("exam %d: domain counts %s, want %s" % (n, got, want))
        ver = hashlib.sha256("|".join(q for _, q, _ in qs).encode("utf-8")).hexdigest()[:8]
        data["exams"][n] = {"title": ex["title"], "min": ex["minutes"], "target": ex["target"], "v": ver,
                            "q": [{"s": s_, "q": q, "a": 0, "o": [{"t": o, "why": w} for o, w in opts]} for s_, q, opts in qs]}
    deck_tpl = open(os.path.join(HERE, "deck.html"), encoding="utf-8").read()
    fonts = {"F_DISP": b64("assets/fonts/bricolage.woff2"), "F_BODY": b64("assets/fonts/figtree.woff2"), "F_MONO": b64("assets/fonts/jetbrains.woff2")}
    logo_small, logo_big, icon32 = b64("assets/logo-transparent-64.png"), b64("assets/logo-transparent-256.png"), b64("assets/icon-32.png")
    deck_files = []

    for n, s in sorted(sessions.items()):
        assert s["id"] == n
        deck_path = "decks/%02d-%s.html" % (n, s["slug"])
        data["content"][n] = {
            "lead": inline(s["lead"]),
            "html": body_html(s["body"]),
            "takeaways": [inline(t) for t in s["takeaways"]],
            "practice": inline(s["practice"]),
            "deck": deck_path,
            "quiz": [{"q": q["q"], "multi": bool(q.get("multi")), "o": [{"t": o[0], "ok": bool(o[1]), "why": o[2]} for o in q["options"]]} for q in s["quiz"]],
        }
        slides = "\n".join(slide_html(sl, s, logo_big) for sl in s["deck"])
        page = deck_tpl.replace("%%SLIDES%%", slides).replace("%%TITLE%%", esc(s["short"]))
        page = page.replace("%%LOGO%%", logo_small).replace("%%ICON32%%", icon32)
        for k, v in fonts.items():
            page = page.replace("%%" + k + "%%", v)
        with open(os.path.join(ROOT, deck_path), "w", encoding="utf-8") as f:
            f.write(page)
        deck_files.append(deck_path)

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = open(os.path.join(HERE, "handout.html"), encoding="utf-8").read().replace("%%DATA%%", payload).replace("%%BASE%%", BASE)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)

    manifest = {
        "name": "Claude Foundations training", "short_name": "Foundations",
        "description": "32 short sessions with practice questions for the CCAO-F exam.",
        "start_url": "./", "scope": "./", "display": "standalone", "orientation": "any",
        "background_color": "#0A162B", "theme_color": "#0A162B",
        "icons": [
            {"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    with open(os.path.join(ROOT, "manifest.webmanifest"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    shell = ["./", "index.html", "manifest.webmanifest", "assets/fonts/bricolage.woff2", "assets/fonts/figtree.woff2",
             "assets/fonts/jetbrains.woff2", "assets/logo-transparent-64.png", "assets/logo-transparent-1024.png",
             "assets/icon-32.png", "assets/icon-180.png", "assets/icon-192.png", "assets/icon-512.png", "assets/favicon.ico"] + deck_files
    digest = hashlib.sha256()
    for p in ["index.html"] + deck_files:
        digest.update(open(os.path.join(ROOT, p), "rb").read())
    sw = SW.replace("%%VER%%", digest.hexdigest()[:10]).replace("%%FILES%%", json.dumps(shell))
    with open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8") as f:
        f.write(sw)
    print("built: index.html, %d decks, cache %s" % (len(deck_files), digest.hexdigest()[:10]))


SW = """// Generated by src/build.py. Pages are fetched fresh when online and served from cache when offline.
const CACHE = 'ct-%%VER%%';
const FILES = %%FILES%%;
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  const isPage = req.mode === 'navigate' || req.url.endsWith('.html');
  if (isPage) {
    e.respondWith(fetch(req).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return r; })
      .catch(() => caches.match(req, {ignoreSearch: true}).then(r => r || caches.match('index.html'))));
  } else {
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })));
  }
});
"""

if __name__ == "__main__":
    main()
