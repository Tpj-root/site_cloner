import sys
from bs4 import BeautifulSoup

def html_to_txt(input_file, output_file):
    """Convert HTML content to plain text and save to the output file."""
    try:
        # Read the HTML content from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get the text only
        text_only = soup.get_text(separator='\n', strip=True)
        
        # Write the extracted text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text_only)
        
        print(f"Text successfully extracted and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html_to_txt.py <inputfile.html> <output.txt>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        html_to_txt(input_file, output_file)

