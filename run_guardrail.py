from pocketflow import Flow

from guardrail.nodes import GuardrailNode, LLMNode, UserInputNode


def main():
    # Create the flow with nodes and connections
    user_input_node = UserInputNode()
    guardrail_node = GuardrailNode()
    llm_node = LLMNode()
    flow = Flow(start=user_input_node)

    # Create flow connections
    user_input_node - "validate" >> guardrail_node
    guardrail_node - "retry" >> user_input_node  # Loop back if input is invalid
    guardrail_node - "process" >> llm_node
    llm_node - "continue" >> user_input_node  # Continue conversation

    shared = {}
    flow.run(shared)


if __name__ == "__main__":
    main()
