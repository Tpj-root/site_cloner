import os
import requests
from bs4 import BeautifulSoup
import time

input_file = "movie_urls.txt"  # Text file containing movie URLs
base_dir = "movies"
ignore_keywords = ["alertmessage", "links", "alert"]
delay_time = 10  # Delay time in seconds

# Create base directory if it doesn't exist
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Function to download lyrics pages
def download_lyrics(movie_name, lyrics_urls):
    movie_dir = os.path.join(base_dir, movie_name)
    if not os.path.exists(movie_dir):
        os.makedirs(movie_dir)
    
    for lyrics_url in lyrics_urls:
        # Ignore URLs with specific keywords
        if any(keyword in lyrics_url for keyword in ignore_keywords):
            print(f"Ignored: {lyrics_url}")
            continue

        # Check if the lyrics_url is valid
        if not lyrics_url.startswith("http"):
            print(f"Invalid URL: {lyrics_url}")
            return

        response = requests.get(lyrics_url)
        if response.status_code == 200:
            lyrics_name = lyrics_url.split("/")[-2].split("?")[0] + ".html"  # Remove query parameters
            file_path = os.path.join(movie_dir, lyrics_name)
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(response.text)
            print(f"Downloaded: {lyrics_url} to {file_path}")
        else:
            print(f"Failed to download: {lyrics_url}")

# Read movie URLs from file
with open(input_file, "r", encoding='utf-8') as file:
    movie_urls = file.readlines()

# Loop through each movie URL
for movie_url in movie_urls:
    movie_url = movie_url.strip()

    # Check if the movie_url is valid
    if not movie_url.startswith("http"):
        print(f"Invalid URL: {movie_url}. Stopping loop.")
        break

    response = requests.get(movie_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        movie_name = movie_url.split("/")[-2]
        lyrics_links = soup.find_all("a", href=True)
        lyrics_urls = [link['href'] for link in lyrics_links if "/lyrics/" in link['href']]
        
        if lyrics_urls:
            download_lyrics(movie_name, lyrics_urls)
        else:
            print(f"No lyrics found for: {movie_name}")
    else:
        print(f"Failed to retrieve movie page: {movie_url}")

    # Introduce a delay before processing the next movie
    time.sleep(delay_time)

