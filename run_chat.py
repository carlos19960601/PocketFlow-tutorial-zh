from pocketflow import Flow

from chat.node import ChatNode

# Create the flow with self-loop
chatNode = ChatNode()
chatNode - "continue" >> chatNode

flow = Flow(start=chatNode)

if __name__ == "__main__":
    shared = {}
    flow.run(shared)
