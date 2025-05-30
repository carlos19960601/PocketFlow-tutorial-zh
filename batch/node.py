import os

from pocketflow import BatchNode

from batch.utils import call_llm


class TranslateTextNode(BatchNode):
    def prep(self, shared):
        text = shared.get("text", "(No text provided)")
        languages = shared.get(
            "languages",
            [
                "Chinese",
                "Spanish",
                "Japanese",
                "German",
                "Russian",
                "Portuguese",
                "French",
                "Korean",
            ],
        )

        # Create batches for each language translation
        return [(text, lang) for lang in languages]

    def exec(self, data_tuple):
        text, language = data_tuple

        prompt = f"""
Please translate the following markdown file into {language}. 
But keep the original markdown format, links and code blocks.
Directly return the translated text, without any other text or comments.

Original: 
{text}

Translated:"""

        result = call_llm(prompt)
        print(f"Translated {language} text")
        return {"language": language, "translation": result}

    def post(self, shared, prep_res, exec_res_list):
        # Create output directory if it doesn't exist
        output_dir = shared.get("output_dir", "translations")
        os.makedirs(output_dir, exist_ok=True)

        # Write each translation to a file
        for result in exec_res_list:
            language, translation = result["language"], result["translation"]

            # Write to file
            filename = os.path.join(output_dir, f"README_{language.upper()}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(translation)

            print(f"Saved translation to {filename}")

    