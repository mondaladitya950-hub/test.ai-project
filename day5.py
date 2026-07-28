

import csv
from google import genai

print("=== AI Data Pipeline (CSV to CSV) ===")

# 1. Authenticate
API_KEY = input("Enter your Google API Key to authenticate: ")
client = genai.Client(api_key=API_KEY)

# 2. Define our input and output files
input_file = "clients.csv"
output_file = "final_results.csv"

try:
    # 3. Open both files simultaneously: one to read, one to write
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        
        # Extract the original column headers and add our new AI column
        fieldnames = reader.fieldnames + ["Generated Hook"]
        
        # Set up the writer and create the top header row
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # 4. The Automation Loop
        for row in reader:
            b_name = row["Business Name"]
            b_type = row["Type"]
            
            print(f"[*] Generating hook for {b_name}...")
            
            # Create the dynamic prompt and call the AI
            prompt = f"Write a punchy, 1-sentence marketing hook for '{b_name}', which is a {b_type}."
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            
            # Clean the response
            hook = response.text.strip()
            
            # Add the generated hook to the current row's data
            row["Generated Hook"] = hook
            
            # Write the complete row to the new output CSV
            writer.writerow(row)
            
    print(f"\n[+] SUCCESS: Data pipeline complete! Open '{output_file}' to see the results.")
        
except FileNotFoundError:
    print(f"\n[-] Error: Could not find '{input_file}'. Make sure it exists in the same folder.")
except Exception as e:
    print(f"\n[-] An unexpected error occurred: {e}")