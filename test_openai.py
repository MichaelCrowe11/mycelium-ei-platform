from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Retrieve OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test OpenAI API
try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Describe how fungi can restore the environment.",
        max_tokens=100
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"Error: {e}"))