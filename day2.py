from google import genai

# 1. Ask the user for the business type
user_topic = input("Enter a business type (e.g., Real Estate, Coffee Shop): ")

# 2. Inject the user's answer into a dynamic prompt using an f-string
dynamic_prompt = f"Write a 2-sentence marketing hook for a {user_topic}."

# 3. Authenticate with your API key
client = genai.Client(api_key=" ")

# 4. Send the dynamic prompt to the AI
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=dynamic_prompt
)

# 5. Print the customized response
print(f"\n--- Your Custom Hook ---")
print(response.text)