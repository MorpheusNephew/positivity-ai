# Positivity AI

An application that uses AI to provide encouraging, thoughtful responses to user prompts.

This is also a learning-first project for exploring AI engineering: building a backend,
working with model APIs, designing prompts, adding safety boundaries, and shipping a small
application end to end.

## Current status

The backend is a Python 3.11 learning project with provider-neutral generation
contracts, provider adapters, and SDK client wrappers for OpenAI and Gemini.
The interactive CLI lets a user select an available provider and model. Each
adapter returns a normalized response containing the provider, model, text, and
total token count. Client construction and API-key lookup are centralized in a
shared client-factory registry.

## Learning roadmap

1. Compare provider behavior, model settings, API keys, and cost.
2. Design and evaluate positivity-oriented prompts.
3. Add safety boundaries appropriate for a wellbeing-oriented application.
4. Wrap the model interaction in a web API, then add a simple user interface.
5. Expand unit coverage and add continuous integration.

## Project notes

Personal lessons and questions live in [LEARNINGS.md](LEARNINGS.md). Collaboration
guidance for Codex and future contributors lives in [AGENTS.md](AGENTS.md).
