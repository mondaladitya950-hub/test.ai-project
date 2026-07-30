
import requests
from google import genai

print("=== The Cloud AI Pipeline ===")

# 1. Authenticate the AI
API_KEY = input("Enter your Google API Key to authenticate: ")
client = genai.Client(api_key=API_KEY)

# 2. Pull Cloud Data (Simulating a client's CRM)
print("\n[*] Fetching new leads from the cloud CRM...")
api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)

# 3. Check connection and process data
if response.status_code == 200:
    leads = response.json()
    print(f"[+] Successfully found {len(leads)} leads!\n")
    
    # 4. The Cloud-to-AI Loop
    for lead in leads[:3]:  # Processing just the first 3 to save time
        name = lead["name"]
        company = lead["company"]["name"]
        
        # We will use the company's "catchPhrase" as their industry/niche
        niche = lead["company"]["catchPhrase"] 
        
        print(f"[*] Drafting personalized email for {name} at {company}...")
        
        # Create the dynamic prompt combining cloud data and our sales pitch
        prompt = (f"Write a short, friendly 2-sentence cold email to {name} who works at {company}. "
                  f"Their company focuses on '{niche}'. Offer our AI data pipeline services to help them scale.")
        
        # Call the AI model
        ai_response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        
        # Output the final result
        print(f"\n--- Drafted Email ---")
        print(ai_response.text.strip())
        print("-" * 50 + "\n")
        
else:
    print(f"[-] Error: Could not connect to CRM. Status Code: {response.status_code}")