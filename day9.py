
import requests
from google import genai

print("=== The End-to-End Cloud AI Pipeline ===")

# 1. Authenticate the AI
API_KEY = input("Enter your Google API Key: ")
client = genai.Client(api_key=API_KEY)

# 2. THE PULL (Fetch a specific lead from the CRM)
print("\n[*] Step 1: Fetching new lead from cloud database...")
pull_url = "https://jsonplaceholder.typicode.com/users/4" # Grabbing lead #4
pull_response = requests.get(pull_url)

if pull_response.status_code == 200:
    lead = pull_response.json()
    name = lead["name"]
    company = lead["company"]["name"]
    print(f"[+] Success! Found lead: {name} at {company}")
    
    # 3. THE PROCESS (Generate the AI Email)
    print("\n[*] Step 2: Drafting personalized email with AI...")
    prompt = f"Write a short, punchy 1-sentence cold email to {name} at {company}. Offer to build them an automated data pipeline."
    
    ai_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    email_draft = ai_response.text.strip()
    print(f"[+] Draft generated:\n  > {email_draft}")
    
    # 4. THE PUSH (Save the generated email back to the CRM)
    print("\n[*] Step 3: Pushing completed draft back to the cloud CRM...")
    push_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Packaging our data exactly how the server wants it
    payload = {
        "title": f"AI Draft for {name}",
        "body": email_draft,
        "userId": lead["id"]
    }
    
    push_response = requests.post(push_url, json=payload)
    
    if push_response.status_code == 201:
        print("[+] Success! The pipeline is complete. Here is the server's receipt:")
        print(push_response.json())
    else:
        print(f"[-] Error pushing data. Status Code: {push_response.status_code}")

else:
    print(f"[-] Error pulling data. Status Code: {pull_response.status_code}")