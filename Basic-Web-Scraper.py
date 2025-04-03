import requests
from bs4 import BeautifulSoup

def fetch_page_title():
    """Enhanced Web Scraper with Error Handling, URL Validation, and Additional Info."""
    url = input("Enter URL: ").strip()
    
    if not url.startswith("http"):
        url = "https://" + url  # Auto-correct URL format
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for failed requests
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string.strip() if soup.title else "No title found"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"].strip() if meta_desc else "No meta description found"
    
    print(f"\nPage Title: {title}")
    print(f"Meta Description: {description}")
    
    # Log the fetched information
    with open("web_scraper_log.txt", "a") as log_file:
        log_file.write(f"URL: {url}\nTitle: {title}\nMeta Description: {description}\n\n")
    
if __name__ == "__main__":
    fetch_page_title()

