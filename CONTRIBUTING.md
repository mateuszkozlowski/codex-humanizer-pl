# Contributing

Thanks for helping improve `humanizer-pl`.

## Before opening a pull request

Please keep changes focused and explain the user-facing reason for the change. Do not include private source text, API keys, telemetry, or automatic installation of Ollama/model data.

Run the deterministic checks from the repository root:

```bash
python3 evals/run_evals.py
python3 evals/run_qa.py
```

If you change humanization behavior, add or update a small regression case. Preserve facts, numbers, URLs, citations, protected fragments, deliberate jargon, and the author's voice. Keep the original examples and upstream attribution intact unless a change is necessary and documented.

## Pull requests

Use the pull request template. Include the reasoning behind behavior changes, the checks you ran, and any known false positives or limitations. Documentation-only changes are welcome when they make installation or safe use clearer.

## Attribution

This repository is a Codex-oriented port of [`pielas-activy/humanizer-pl`](https://github.com/pielas-activy/humanizer-pl), with English patterns derived from [`blader/humanizer`](https://github.com/blader/humanizer). Please preserve the notices and licenses when modifying or redistributing the project.
