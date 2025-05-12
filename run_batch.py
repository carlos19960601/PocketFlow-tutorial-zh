import time

from pocketflow import Flow

from batch.node import TranslateTextNode


def main():
    # read the text from ../../README.md
    with open("./batch/README.md", "r") as f:
        text = f.read()

    # Default settings
    shared = {
        "text": text,
        "languages": [
            "Chinese",
            # "Spanish",
            "Japanese",
            # "German",
            # "Russian",
            # "Portuguese",
            # "French",
            # "Korean",
        ],
        "output_dir": "./batch/translations",
    }
    # --- Time Measurement Start ---
    print(
        f"Starting sequential translation into {len(shared['languages'])} languages..."
    )
    start_time = time.perf_counter()

    # Run the translation flow
    translate_node = TranslateTextNode(max_retries=3)
    flow = Flow(start=translate_node)
    flow.run(shared)

    # --- Time Measurement End ---
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(
        f"\nTotal sequential translation time: {duration:.4f} seconds"
    )  # Print duration
    print("\n=== Translation Complete ===")
    print(f"Translations saved to: {shared['output_dir']}")
    print("============================")


if __name__ == "__main__":
    main()
