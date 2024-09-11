import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class GrammarCheckTool:
    @staticmethod
    @tool("Check grammar and style")
    def check_grammar(text):
        """Useful to check and correct grammatical errors in a text content."""
        api_key = os.environ.get('GRAMMAR_API_KEY')  # Ensure your API key is stored in environment variables
        url = "https://api.grammarcheck.com/check"  # Placeholder API endpoint

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
            corrections = response.json()  # Parsing response to get corrections
            corrected_text = GrammarCheckTool.apply_corrections(text, corrections)
            return corrected_text
        else:
            error_message = response.json().get('message', 'Failed to check grammar')
            raise Exception(f"Grammar check failed with error: {error_message}")

    @staticmethod
    def apply_corrections(original_text, corrections):
        """Applies corrections to the original text based on API response."""
        # This function assumes a simple replacement process. It should be adapted based on the actual structure of the API response.
        for correction in corrections.get('corrections', []):
            original_text = original_text.replace(correction['incorrect'], correction['correct'])

        return original_text

# import re

# class GrammarCheckTool:
#     @staticmethod
#     def check_grammar(text):
#         """Apply simple grammar checks and corrections."""
#         text = GrammarCheckTool.capitalize_sentences(text)
#         text = GrammarCheckTool.add_punctuation(text)
#         text = GrammarCheckTool.correct_common_mistakes(text)
#         return text

#     @staticmethod
#     def capitalize_sentences(text):
#         """Capitalize the first letter of each sentence."""
#         # Using regex to capitalize first characters of each sentence
#         return re.sub(r'(?<!\w)([a-z])', lambda x: x.group().upper(), text)

#     @staticmethod
#     def add_punctuation(text):
#         """Ensure text ends with a punctuation mark."""
#         if not re.match(r'.*[.!?]$', text.strip()):
#             return text.strip() + '.'
#         return text

#     @staticmethod
#     def correct_common_mistakes(text):
#         """Correct common spelling mistakes."""
#         corrections = {
#             'teh': 'the',
#             'realy': 'really',
#             'wierd': 'weird',
#             'definately': 'definitely',
#             'recieve': 'receive',
#         }
#         # Using regex for word boundary to replace whole words only
#         pattern = re.compile(r'\b(' + '|'.join(corrections.keys()) + r')\b')
#         return pattern.sub(lambda x: corrections[x.group()], text)
