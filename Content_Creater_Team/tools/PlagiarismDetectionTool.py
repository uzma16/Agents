import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class PlagiarismDetectionTool:
    @staticmethod
    @tool("Detect and edit plagiarized content")
    def scan_for_plagiarism(text):
        """Detects plagiarism and edits the text to remove or paraphrase plagiarized sections."""
        api_key = os.environ.get('PLAGIARISM_API_KEY')  # Ensure your API key is stored in environment variables
        url = "https://api.plagiarismchecker.com/detect"  # Placeholder API endpoint

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "text": text,
            "language": "en"  # Assuming the API requires a language code
        })

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            plagiarism_report = response.json()  # Parsing response to get plagiarism details
            return PlagiarismDetectionTool.edit_plagiarized_content(text, plagiarism_report)
        else:
            error_message = response.json().get('message', 'Failed to detect plagiarism')
            raise Exception(f"Plagiarism detection failed with error: {error_message}")

    @staticmethod
    def edit_plagiarized_content(original_text, report):
        """Edits the original text by removing or paraphrasing plagiarized sections."""
        if report.get('is_plagiarized'):
            # This is a placeholder for the editing process. The actual implementation depends on the response structure and needs.
            for instance in report.get('instances', []):
                # Here we simply remove the plagiarized text. You might want to replace it with a paraphrase.
                plagiarized_text = instance['text']
                original_text = original_text.replace(plagiarized_text, "[Text removed due to plagiarism concerns]")
        return original_text
