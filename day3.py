from google import genai

class ClientManager:
    """Manages client data and saves AI-generated hooks to a file."""
    
    def __init__(self):
        # Dictionary to store all client data
        self.database = {}

    def add_client(self, client_id, business_type, owner_name):
        # Tuple for immutable data (business_type, owner_name)
        # List for mutable data (hooks)
        self.database[client_id] = {
            "info": (business_type, owner_name),
            "hooks": [] 
        }
        print(f"[*] Client {owner_name} ({business_type}) added to the system.")

    def add_hook(self, client_id, hook_text):
        # Append the new hook to the client's list
        if client_id in self.database:
            self.database[client_id]["hooks"].append(hook_text)

    def save_to_file(self, filename):
        # Error and File handling for safe saving
        try:
            with open(filename, "a") as file:
                for client_id, data in self.database.items():
                    b_type = data["info"][0]
                    owner = data["info"][1]
                    
                    file.write(f"\n--- AI Hooks for {owner} ({b_type}) ---\n")
                    for hook in data["hooks"]:
                        file.write(f"- {hook}\n\n")
                        
            print(f"[+] Success: All hooks safely saved to {filename}")

        except PermissionError:
            print("[-] Error: You lack the necessary permissions to write to this file.")
        except Exception as e:
            print(f"[-] An unexpected error occurred: {e}")

# ==========================================
# MAIN AUTOMATION SCRIPT
# ==========================================

print("=== AI Marketing Automation System ===")

# 1. Initialize the API and the Manager
API_KEY = input("Enter your Google API Key to authenticate: ")
ai_client = genai.Client(api_key=API_KEY)
agency_manager = ClientManager()

# 2. Gather client details using input()
print("\n--- New Client Setup ---")
c_id = input("Enter Client ID (e.g., C-001): ")
b_type = input("Enter Business Type (e.g., Dental Clinic): ")
owner = input("Enter Owner's Name (e.g., Dr. Smith): ")

# 3. Store the client in our OOP database
agency_manager.add_client(client_id=c_id, business_type=b_type, owner_name=owner)

# 4. Generate the hook using the API
print(f"\n[*] Generating marketing hook for {b_type}...")
dynamic_prompt = f"Write a 2-sentence marketing hook for a {b_type}."

response = ai_client.models.generate_content(
    model="gemini-3.6-flash",
    contents=dynamic_prompt
)
generated_hook = response.text.strip()
print(f"[+] AI Hook Generated: {generated_hook}")

# 5. Add the hook to the dictionary and save to file
agency_manager.add_hook(client_id=c_id, hook_text=generated_hook)
agency_manager.save_to_file("agency_hooks.txt")

print("=== Process Complete ===")