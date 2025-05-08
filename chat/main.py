from pocketflow import Flow, Node


class ChatNode(Node):
    def prep(self, shared):
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Welcome to the chat! Type 'exit' to end the conversation.")

        # Get user input
        user_input = input("\nYou: ")
        


chatNode = ChatNode()
flow = Flow(start=chatNode)

if __name__ == "__main__":
    shared = {}
    flow.run(shared)
