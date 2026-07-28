import csv
from google import genai

print("=== AI Batch Processing Engine ===")

# 1. Authenticate
API_KEY = input("Enter your Google API Key to authenticate: ")
client = genai.Client(api_key=API_KEY)

# 2. Open a new text file to save our results
with open("batch_results.txt", "w") as output_file:
    output_file.write("=== AUTOMATED AGENCY HOOKS ===\n\n")

    # 3. Open and read our spreadsheet (CSV) safely
    try:
        with open("clients.csv", "r") as csv_file:
            # DictReader turns each spreadsheet row into a dictionary
            reader = csv.DictReader(csv_file)
            
            # 4. THE AUTOMATION LOOP
            for row in reader:
                # Extract data using the exact column names from your CSV
                b_name = row["Business Name"]
                b_type = row["Type"]
                
                print(f"\n[*] Processing {b_name} ({b_type})...")
                
                # Create the dynamic prompt
                prompt = f"Write a punchy, 1-sentence marketing hook for '{b_name}', which is a {b_type}."
                
                # Call the AI model
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )
                
                # Clean the response and print it
                hook = response.text.strip()
                print(f"[+] AI Hook: {hook}")
                
                # Save it to our text file
                output_file.write(f"Business: {b_name} ({b_type})\n")
                output_file.write(f"Hook: {hook}\n")
                output_file.write("-" * 40 + "\n")
                
        # This prints only after the loop finishes all rows
        print("\n[+] SUCCESS: All clients processed! Check batch_results.txt")
        
    except FileNotFoundError:
        print("\n[-] Error: Could not find 'clients.csv'. Did you create it in the exact same folder?")