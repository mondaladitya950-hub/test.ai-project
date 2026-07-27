from google import genai

# 1. Authenticate with your new API key
client = genai.Client(api_key=" ")

# 2. Send the prompt to the newest AI model
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a 2-sentence marketing hook for a digital marketing agency."
)

# 3. Print the response to your terminal
print(response.text)