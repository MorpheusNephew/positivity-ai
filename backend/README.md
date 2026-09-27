# Positivity AI backend

The Python backend for Positivity AI. It is a learning-first project for building
a provider-agnostic application that sends user prompts to AI models and returns
encouraging, thoughtful responses.

## Structure

```text
src/positivity_ai/
  adapters/    Provider-specific integrations for OpenAI and Gemini
  clients/     Provider SDK wrappers and the shared client-factory registry
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

Run the unit tests:

```bash
poetry run pytest -q
```

## Current scope

The backend can send requests through OpenAI and Gemini provider clients. The
interactive CLI lets users select an available provider and model. Each adapter
normalizes its provider response into a `GenerationResponse` containing the
provider, model, assistant text, and total token count.

`ClientManager` centralizes provider SDK construction and reads
`OPENAI_API_KEY` or `GEMINI_API_KEY` when an adapter is created without an
explicit API key. The pytest suite uses mocks, so its 17 unit tests run without
provider credentials or live API calls.
