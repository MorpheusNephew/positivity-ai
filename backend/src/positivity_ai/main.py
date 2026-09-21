"""Command-line entry point for experimenting with Positivity AI."""

from importlib.resources import files

from positivity_ai.adapters.manager import AdapterManager
from positivity_ai.generation.types import GenerationRequest, Message

# Conversation history retained across turns of the interactive CLI session.
stored_messages: list[Message] = []


def select_numbered_option(label: str, options: list[str]) -> str:
    """Display ``options`` and return the value selected by its number."""
    if not options:
        raise ValueError(f"No {label}s are available.")

    print(f"Available {label}s:")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        selection = input(f"Select a {label} by number: ")

        try:
            selected_number = int(selection)
        except ValueError:
            print("Please enter a number from the list.")
            continue

        if 1 <= selected_number <= len(options):
            return options[selected_number - 1]

        print("Please enter a number from the list.")


def load_prompt(prompt_name: str) -> str:
    """Load a Markdown prompt bundled with the installed application package."""
    prompt_file = files("positivity_ai").joinpath("prompts", prompt_name)

    return prompt_file.read_text(encoding="utf-8")


def main() -> None:
    """Run the interactive command-line experiment."""
    print("Hello Positive World")
    print("Welcome to your positive AI Bot")

    selection = ""

    system_prompt = load_prompt("positivity_v1.md")
    provider = select_numbered_option(
        "provider", AdapterManager.get_available_providers()
    )
    adapter_class = AdapterManager.get_adapter_class(provider)
    adapter = adapter_class()

    model = select_numbered_option("model", adapter.get_models_list())

    while selection.lower() != "exit":
        selection = input("Would you like some motivation? ")

        if selection.lower() == "no":
            break

        new_message = Message(role="user", content=selection)

        stored_messages.append(new_message)

        response = adapter.generate(
            GenerationRequest(
                provider=provider,
                model=model,
                messages=stored_messages,
                system_prompt=system_prompt,
            )
        )

        print(response)


if __name__ == "__main__":
    main()
