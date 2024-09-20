import os
import sys
import requests
import csv
import time
from bs4 import BeautifulSoup

# Function to process a single page and extract movie details
def process_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    # Find all divs containing the required class
    for tag in soup.find_all(class_="col-lg-5 col-sm-5 col-xs-5 big-font"):
        # Extract the URL
        link_tag = tag.find('a', href=True)
        if link_tag:
            movie_url = link_tag['href']
            movie_name = link_tag.text.strip()

        # Find the corresponding year in the nearby div with the specified class
        year_tag = tag.find_next_sibling(class_="col-lg-2 col-sm-2 col-xs-2")
        if year_tag:
            year = year_tag.text.strip()

        # Append the movie details to the data list
        data.append([movie_url, movie_name, year])

    return data

# Main function to loop through pages and save the result to a CSV file
def scrape_pages(start_page, end_page, output_file):
    all_data = []

    # Loop through the specified page range
    for page_num in range(start_page, end_page + 1):
        url = f"https://www.tamil2lyrics.com/movie/page/{page_num}/"
        print(f"Processing page: {url}")
        page_data = process_page(url)
        all_data.extend(page_data)

        # Delay of 5 seconds between requests
        time.sleep(5)

    # Save the data to the CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Movie URL", "Movie Name", "Year"])
        csvwriter.writerows(all_data)

    print(f"Data saved to {output_file}")

# Parameters for start and end page
start_page = 1
end_page = 271
output_file = "movie_details.csv"

# Run the scraping function
scrape_pages(start_page, end_page, output_file)

