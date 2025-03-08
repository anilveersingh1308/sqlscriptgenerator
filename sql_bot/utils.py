import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def query_groq_api(user_query):
    url = "https://api.openai.com/v1/chat/completions"  # Correct endpoint

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",  # Use a supported model
        "messages": [{"role": "user", "content": user_query}]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an error for non-200 responses

        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        logger.error(f"Response content: {response.content if response else 'No response'}")
        return f"API Error: {str(e)}"
