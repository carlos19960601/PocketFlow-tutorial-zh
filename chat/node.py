from pocketflow import Node

from chat.utils import call_llm


class ChatNode(Node):
    def prep(self, shared):
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Welcome to the chat! Type 'exit' to end the conversation.")

        # Get user input
        user_input = input("\nYou: ")

        # Check if user wants to exit
        if user_input.lower() == "exit":
            return None

        # Add user message to history
        shared["messages"].append({"role": "user", "content": user_input})

        # Return all messages for the LLM
        return shared["messages"]

    def exec(self, messages):
        if messages is None:
            return None

        # Call LLM with the entire conversation history
        response = call_llm(messages)
        return response

    def post(self, shared, prep_res, exec_res):
        if prep_res is None or exec_res is None:
            print("\nGoodbye!")
            return None  # End the conversation

        # Print the assistant's response
        print(f"\nAssistant: {exec_res}")

        # Add assistant message to history
        shared["messages"].append({"role": "assistant", "content": exec_res})

        # Loop back to continue the conversation
        return "continue"
