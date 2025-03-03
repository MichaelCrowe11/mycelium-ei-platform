from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Retrieve OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test OpenAI API with the ChatCompletion endpoint
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an environmental AI assistant."},
        {"role": "user", "content": "Describe how fungi can restore the environment."}
    ],
    max_tokens=100
)

print(response.choices[0].text.strip())
# Print the response
print(response.choices[0].message["content"].strip())
