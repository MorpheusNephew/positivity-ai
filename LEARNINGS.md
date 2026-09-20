# Learnings

Use this as a lightweight, dated record of things you learn, questions you want to revisit,
and decisions you make while building Positivity AI.

## Entries

### 2026-09-20 — Build one provider by hand, then use it as an AI-assisted blueprint

I first wrote the OpenAI adapter and client from scratch. Building that path by
hand gave me a working understanding of the provider-neutral request and
response contracts, the adapter/client boundary, and provider error handling.

Now that I understand that architecture, I can use the OpenAI implementation as
a blueprint when asking AI to help create another provider implementation, such
as Gemini. This lets me leverage AI for the repetitive translation work without
skipping the architectural understanding. I should still compare the generated
code against the blueprint, understand provider-specific differences, and test
the result before relying on it.
