# positivity-ai

An application that uses AI to provide encouraging, thoughtful responses to user prompts.

This is also a learning-first project for exploring AI engineering: building a backend,
working with model APIs, designing prompts, adding safety boundaries, and shipping a small
application end to end.

## Current status

The backend is a Python 3.11 learning project with provider-neutral generation
contracts and a shared client protocol. It currently includes OpenAI and Gemini
adapter/client implementations. The interactive CLI uses OpenAI, and adapters
still return a temporary normalized response while raw provider-response
translation is being completed.

## Learning roadmap

1. Finish translating raw provider responses into reliable, structured output.
2. Compare provider behavior, model settings, API keys, and cost.
3. Design and evaluate positivity-oriented prompts.
4. Add safety boundaries appropriate for a wellbeing-oriented application.
5. Wrap the model interaction in a web API, then add a simple user interface and tests.

## Project notes

Personal lessons and questions live in [LEARNINGS.md](LEARNINGS.md). Collaboration
guidance for Codex and future contributors lives in [AGENTS.md](AGENTS.md).
