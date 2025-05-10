from workflow.flow import create_article_flow


def run_flow(topic="AI Safety"):
    """
    Run the article writing workflow with a specific topic

    Args:
        topic (str): The topic for the article
    """
    # Initialize shared data with the topic
    shared = {"topic": topic}
    # Print starting message
    print(f"\n=== Starting Article Workflow on Topic: {topic} ===\n")

    # Run the flow
    flow = create_article_flow()
    flow.run(shared)


if __name__ == "__main__":
    import sys

    # Get topic from command line if provided
    topic = "AI Safety"  # Default topic
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])

    run_flow(topic)
