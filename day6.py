
import requests

print("=== Cloud API Data Puller ===")

# 1. The URL is the "address" of the data we want to pull
api_url = "https://jsonplaceholder.typicode.com/users"

print("[*] Contacting the server...")

# 2. Make the "Pull" request
response = requests.get(api_url)

# 3. Check if the server answered successfully (Status Code 200 means OK)
if response.status_code == 200:
    print("[+] Connection Successful!\n")
    
    # Convert the internet response into a Python list/dictionary (JSON)
    leads = response.json()
    
    print(f"We found {len(leads)} leads in the cloud database. Here are the first 3:\n")
    
    # 4. The Loop (Just like your CSV loop!)
    for lead in leads[:3]:  # The [:3] just tells it to stop after 3
        name = lead["name"]
        company = lead["company"]["name"]
        email = lead["email"]
        
        print(f"Lead Name: {name}")
        print(f"Company: {company}")
        print(f"Email: {email}")
        print("-" * 30)

else:
    print(f"[-] Error: Could not connect. Status Code: {response.status_code}")