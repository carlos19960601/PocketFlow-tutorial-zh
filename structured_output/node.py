from pocketflow import Node

from structured_output.utils import call_llm


class ResumeParserNode(Node):
    def prep(self, shared):
        """Return resume text and target skills from shared state."""
        return {
            "resume_text": shared["resume_text"],
            "target_skills": shared.get("target_skills", []),
        }

    def exec(self, prep_res):
        """Extract structured data from resume using prompt engineering.
        Requests YAML output with comments and skill indexes as a list.
        """
        resume_text = prep_res["resume_text"]
        target_skills = prep_res["target_skills"]

        # print(f"resume_text: \n{resume_text}\n\n target_skills: \n{target_skills}")

        # Format skills with indexes for the prompt
        skill_list_for_prompt = "\n".join(
            [f"{i}: {skill}" for i, skill in enumerate(target_skills)]
        )

        # Simplified Prompt focusing on key instructions and format
        prompt = f"""
Analyze the resume below. Output ONLY the requested information in YAML format.

**Resume:**
```
{resume_text}
```

**Target Skills (use these indexes):**
```
{skill_list_for_prompt}
```

**YAML Output Requirements:**
- Extract `name` (string).
- Extract `email` (string).
- Extract `experience` (list of objects with `title` and `company`).
- Extract `skill_indexes` (list of integers found from the Target Skills list).
- **Add a YAML comment (`#`) explaining the source BEFORE `name`, `email`, `experience`, each item in `experience`, and `skill_indexes`.**

**Example Format:**
```yaml
# Found name at top
name: Jane Doe
# Found email in contact info
email: jane@example.com
# Experience section analysis
experience:
  # First job listed
  - title: Manager
    company: Corp A
  # Second job listed
  - title: Assistant
    company: Corp B
# Skills identified from the target list based on resume content
skill_indexes:
  # Found 0 at top  
  - 0
  # Found 2 in experience
  - 2
```

Generate the YAML output now:
"""
        response = call_llm(prompt)

        return response

    def post(self, shared, prep_res, exec_res):
        """Store structured data and print it."""
        shared["structured_data"] = exec_res
        print(exec_res)
        print("✅ Extracted resume information.")
