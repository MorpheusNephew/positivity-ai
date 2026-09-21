# Positivity AI backend

The Python backend for Positivity AI. It is a learning-first project for building
a provider-agnostic application that sends user prompts to AI models and returns
encouraging, thoughtful responses.

## Structure

```text
src/positivity_ai/
  adapters/    Provider-specific integrations for OpenAI and Gemini
  clients/     Provider SDK wrappers behind a shared client protocol
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

The backend can send requests through OpenAI and Gemini provider clients. The
interactive CLI currently uses OpenAI. Adapters still return a temporary
`GenerationResponse`; the next milestone is translating each provider's raw
response into the provider-neutral response contract.
