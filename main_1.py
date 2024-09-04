import requests
from bs4 import BeautifulSoup
import os
import time

base_url = "https://www.tamil2lyrics.com/movie/page/"
output_dir = "downloaded_pages"
output_file = "movie_urls.txt"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the output file to store the movie URLs
with open(output_file, "w", encoding='utf-8') as url_file:
    for i in range(1, 270):  # Loop from page 1 to 270
        url = f"{base_url}{i}/"
        
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Failed to download: {url} due to {e}")
            time.sleep(5)  # Wait 10 seconds before retrying
            continue

        if response.status_code == 200:
            file_path = os.path.join(output_dir, f"page_{i}.html")
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(response.text)

            # Parse the HTML to find movie URLs
            soup = BeautifulSoup(response.text, "html.parser")
            movie_links = soup.find_all("a", href=True)
            for link in movie_links:
                movie_url = link['href']
                if "/movies/" in movie_url:
                    url_file.write(f"{movie_url}\n")
            print(f"Downloaded and parsed: {url}")
        else:
            print(f"Failed to download: {url}")
        
        # Introduce a delay between requests to avoid overloading the server
        time.sleep(5)

print(f"All movie URLs have been saved to {output_file}.")

