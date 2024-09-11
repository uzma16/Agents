import os
import json
import requests
from crewai import Agent, Task
from langchain.tools import tool


# class NLPTool:
#     @tool("Generate text with AI")
#     def generate_text(platform, description, min_word_length, max_word_length):
#         """Generates text based on the given description & for the given platform using an updated AI chat model, considering additional constraints."""
#         # Retrieve API key securely from environment variables
#         api_key = os.getenv('OPENAI_API_KEY', 'sk-proj-lG2Fk8i7e6nt5N9fNTovT3BlbkFJ74J0EJw5Vooi5pKyMgFT')
#         endpoint = "https://api.openai.com/v1/chat/completions"  # Corrected endpoint for chat models

#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': f'Bearer {api_key}'
#         }

#         # Formulate a message that incorporates the platform, description, and word length constraints
#         message = f"Write an engaging and detailed blog post about {description} for {platform}. The post should be about {description}. Aim for a length between {min_word_length} and {max_word_length} words. Include key points, relevant data, and practical advice."

#         data = {
#             "model": "gpt-3.5-turbo-16k-0613",  
#             "messages": [{"role": "user", "content": message}],  # Use 'messages' field for chat API
#             "max_tokens": max_word_length,
#             "temperature": 0.7,
#             "top_p": 1.0,
#             "frequency_penalty": 0.5,
#             "presence_penalty": 0.0
#         }

#         response = requests.post(endpoint, headers=headers, data=json.dumps(data))
        
#         if response.status_code == 200:
#             # Extract the generated text from the API response
#             generated_text = response.json()['choices'][0]['message']['content'].strip()  # Correct JSON path for chat completions
#             return generated_text
#         else:
#             # Handle any API errors
#             error_message = response.json().get('error', {}).get('message', 'Failed to generate text')
#             raise Exception(f"API request failed with response: {error_message}")


import os
import requests
import json

class NLPTool:
    @tool("Generate text with AI")
    def generate_text(platform, description, min_word_length, max_word_length):
        """Generates text based on the given description & for the given platform using an updated AI chat model, considering additional constraints."""
        
        # Set the Groq API key and base URL
        api_key = os.getenv('GROQ_API_KEY', 'default_api_key')
        base_url = os.getenv('GROQ_API_BASE', 'https://api.groq.com/openai/v1')
        
        # Correct endpoint for Groq's completion model
        endpoint = f"{base_url}/test-endpoint"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        # Formulate a message that incorporates the platform, description, and word length constraints
        message = f"Write an engaging and detailed blog post about {description} for {platform}. The post should be about {description}. Aim for a length between {min_word_length} and {max_word_length} words. Include key points, relevant data, and practical advice."

        data = {
            "model": "gemma-7b-it",  
            "messages": [{"role": "user", "content": message}],
            "max_tokens": max_word_length,
            "temperature": 0.7,
            "top_p": 1.0,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.0
        }

        response = requests.post(endpoint, headers=headers, json=data)  # Use json=data to properly format the request body
        
        if response.status_code == 200:
            # Extract the generated text from the API response
            generated_text = response.json().get('choices', [])[0].get('message', {}).get('content', '').strip()
            return generated_text
        else:
            # Handle any API errors
            error_message = response.json().get('error', {}).get('message', 'Failed to generate text')
            raise Exception(f"API request failed with response: {error_message}")
