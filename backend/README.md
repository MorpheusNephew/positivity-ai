# Positivity AI backend

The Python backend for Positivity AI. It is a learning-first project for building
a provider-agnostic application that sends user prompts to AI models and returns
encouraging, thoughtful responses.

## Structure

```text
src/positivity_ai/
  adapters/    Provider-specific integrations, beginning with OpenAI
  generation/  Provider-neutral request, response, and error contracts
  prompts/     Versioned model instructions
```

## Development

Install the project and its dependencies:

```bash
poetry install
```

Run the current entry point:

```bash
poetry run positivity-ai
```

## Current scope

The backend currently defines the initial package structure and a first
positivity prompt. The next milestone is making a direct model call through
the OpenAI adapter.
