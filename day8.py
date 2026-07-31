
import requests

print("=== The API Data Pusher ===")

# 1. The Target URL (Where are we sending the data?)
# We use the /posts endpoint to simulate saving a record to a database
api_url = "https://jsonplaceholder.typicode.com/posts"

# 2. The Data Payload (What are we sending?)
# We package our data into a Python dictionary
email_draft = {
    "title": "New AI Email Draft for Leanne",
    "body": "Hi Leanne, I've been following Romaguera-Crona's impressive work...",
    "userId": 1
}

print("[*] Pushing the AI draft to the cloud CRM...")

# 3. The POST Request (The Push)
# Notice we use requests.post() instead of requests.get()
response = requests.post(api_url, json=email_draft)

# 4. Check the result 
# Status Code 200 means "OK", but 201 specifically means "Created Successfully!"
if response.status_code == 201:
    print("[+] Success! The data was securely saved to the cloud.")
    print("\nHere is the exact receipt the server sent back:")
    print(response.json())
else:
    print(f"[-] Error: Could not save data. Status Code: {response.status_code}")