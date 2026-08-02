
import requests
import time

print("=== The Enterprise Bulk Extractor ===")

base_url = "https://jsonplaceholder.typicode.com/posts"
all_records = []

# 1. The Pagination Loop (Simulating clicking through 3 pages)
for page in range(1, 4):
    print(f"[*] Fetching Page {page}...")
    
    # 2. Query Parameters: We tell the URL exactly which page we want
    # ?_page=1&_limit=5 means "Give me page 1, and only 5 items at a time"
    paginated_url = f"{base_url}?_page={page}&_limit=5"
    
    response = requests.get(paginated_url)
    
    # 3. Process the Page
    if response.status_code == 200:
        data = response.json()
        
        # 4. The Exit Strategy: Stop if the page is empty
        if not data:
            print("[-] No more data found. Database fully extracted.")
            break
            
        all_records.extend(data) # Add this page's data to our master list
        print(f"[+] Successfully grabbed {len(data)} records from Page {page}.")
        
        # 5. Rate Limiting: Pause for 1 second so the server doesn't block us
        time.sleep(1)
        
    else:
        print(f"[-] Error connecting on Page {page}. Status Code: {response.status_code}")
        break

print(f"\n[+] Extraction Complete! We securely downloaded a total of {len(all_records)} records across all pages.")