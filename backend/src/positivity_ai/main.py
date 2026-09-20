"""Command-line entry point for experimenting with Positivity AI."""

from positivity_ai.adapters import OpenAIAdapter
from positivity_ai.generation import GenerationRequest, Message

# Conversation history retained across turns of the interactive CLI session.
stored_messages: list[Message] = []


def main() -> None:
    """Run the interactive command-line experiment."""
    print("Hello Positive World")
    print("Welcome to your positive AI Bot")

    selection = ""

    openai_adapter = OpenAIAdapter()

    while selection.lower() != "exit":
        selection = input("Would you like some motivation? ")

        if selection.lower() == "no":
            break

        openai_models_list = openai_adapter.get_models_list()

        first_mini = [model for model in openai_models_list if "mini" in model][0]

        new_message = Message(role="user", content=selection)

        stored_messages.append(new_message)

        response = openai_adapter.generate(
            GenerationRequest(
                provider="openai",
                model=first_mini,
                messages=stored_messages,
                system_prompt="Think nicely",
            )
        )

        print(response)


if __name__ == "__main__":
    main()
