from pocketflow import Flow

from streaming.node import StreamNode


def main():
    node = StreamNode()
    flow = Flow(start=node)

    shared = {"prompt": "What's the meaning of life?"}
    flow.run(shared)


if __name__ == "__main__":
    main()
