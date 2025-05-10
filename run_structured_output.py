from pocketflow import Flow

from structured_output.node import ResumeParserNode

if __name__ == "__main__":
    print("=== Resume Parser - Structured Output with Indexes & Comments ===\n")
    # --- Configuration ---
    target_skills_to_find = [
        "Team leadership & management",  # 0
        "CRM software",  # 1
        "Project management",  # 2
        "Public speaking",  # 3
        "Microsoft Office",  # 4
        "Python",  # 5
        "Data Analysis",  # 6
    ]
    resume_file = "./structured_output/data.txt"  # Assumes data.txt contains the resume

    # --- Prepare Shared State ---
    shared = {}
    try:
        with open(resume_file, "r") as file:
            shared["resume_text"] = file.read()
    except FileNotFoundError:
        print(f"Error: Resume file '{resume_file}' not found.")
        exit(1)  # Exit if resume file is missing

    shared["target_skills"] = target_skills_to_find

    parser_node = ResumeParserNode(max_retries=3, wait=10)
    flow = Flow(start=parser_node)
    flow.run(shared)  # Execute the parsing node
