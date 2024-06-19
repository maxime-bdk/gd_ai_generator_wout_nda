import sys
import requests
from bs4 import BeautifulSoup, Comment

def extract_content_between_id_and_footer(url, output_file, start_id, footer_class):
    # Download the HTML content from the URL
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the HTML content. Status code: {response.status_code}")
    
    html_content = response.text
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Check for comments that might contain the footer and extract them
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment_soup = BeautifulSoup(comment, 'html.parser')
        if comment_soup.find(class_=footer_class):
            soup.append(comment_soup)
    
    # Find the start element by ID and the footer element by class
    start_element = soup.find(id=start_id)
    footer_element = soup.find(class_=footer_class)
    
    if not start_element or not footer_element:
        raise ValueError(f"Could not find elements with ID {start_id} and/or class {footer_class}")
    
    # Extract the content between the start ID and the footer class
    extracted_content = ""
    current_element = start_element
    
    while current_element and current_element != footer_element:
        extracted_content += str(current_element)
        current_element = current_element.find_next()
    
    # Add the footer element itself
    extracted_content += str(footer_element)
    
    # Write the extracted content to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(extracted_content)

if __name__ == "__main__":
    # Read command line arguments
    if len(sys.argv) != 5:
        print("Usage: python htmlparser.py <url> <output_file> <start_id> <footer_class>")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = sys.argv[2]
    start_id = sys.argv[3]
    footer_class = sys.argv[4]


extract_content_between_id_and_footer(url, output_file, start_id, footer_class)
