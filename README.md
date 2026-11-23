# Claude Foundations training

Study guide, practice questions and slide decks for the Claude Certified Associate, Foundations (CCAO-F) exam.

Live site: https://thenomadagent.github.io/claude-training/

- `index.html` is the handout app: all sessions, glossary and quizzes in one page. It installs to a phone home screen and works offline.
- `decks/` holds one self-contained slide deck per session. Each file can be opened or emailed on its own.
- `src/` holds the content and the build script. The files above are generated from it.

## Rebuilding

```
npm install qrcode-svg
QR_NODE_PATH=./node_modules python3 src/build.py
```

To add a session, create `src/content/sNN.py` following an existing one and rebuild.

## Notes

Built by Justin VanAusdall. Unofficial study material, not affiliated with or endorsed by Anthropic.
All practice questions are original and are not taken from the exam.
