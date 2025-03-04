import requests
from bs4 import BeautifulSoup
import re

# Function to extract arXiv ID from URL
def extract_arxiv_id(url):
    match = re.search(r'arxiv.org/(?:abs|pdf)/(\d+\.\d+)', url)
    return match.group(1) if match else None

# Replace with the URL of the webpage containing arXiv links
webpage_url = "https://github.com/WLiK/LLM4Rec-Awesome-Papers"

# Fetch the webpage content
response = requests.get(webpage_url)
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

# Parse the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all links
links = soup.find_all("a", href=True)

# Extract arXiv IDs
arxiv_ids = set()
for link in links:
    arxiv_id = extract_arxiv_id(link["href"])
    if arxiv_id:
        arxiv_ids.add(arxiv_id)

# Save to a text file
with open("arxiv_ids.txt", "w") as f:
    for arxiv_id in sorted(arxiv_ids):
        f.write(arxiv_id + "\n")
