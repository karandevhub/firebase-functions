import requests
from bs4 import BeautifulSoup, NavigableString
from typing import Dict, Any
import re

def scrape_webpage(url: str) -> Dict[str, Any]:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements first
        for element in soup.find_all(['script', 'style', 'iframe', 'noscript', 'svg', 
                                    'footer', 'header', 'nav', 'aside', 'form']):
            element.decompose()

        content = []
        
        def process_content(element):
            for child in element.children:
                if not isinstance(child, NavigableString):
                    # Process headings
                    if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                        level = int(child.name[1])
                        text = child.get_text().strip()
                        if text:
                            content.append(f"\n{'#' * level} {text}\n")
                    
                    # Process paragraphs
                    elif child.name == 'p':
                        text = child.get_text().strip()
                        if text:
                            # Check for emphasis elements
                            if child.find(['strong', 'b', 'em', 'i']):
                                content.append(f"*{text}*\n")
                            else:
                                content.append(f"{text}\n")
                    
                    # Process unordered lists
                    elif child.name == 'ul':
                        for li in child.find_all('li', recursive=False):
                            text = li.get_text().strip()
                            if text:
                                if li.find(['strong', 'b', 'em', 'i']):
                                    content.append(f"- *{text}*\n")
                                else:
                                    content.append(f"- {text}\n")
                    
                    # Process ordered lists
                    elif child.name == 'ol':
                        for i, li in enumerate(child.find_all('li', recursive=False), 1):
                            text = li.get_text().strip()
                            if text:
                                if li.find(['strong', 'b', 'em', 'i']):
                                    content.append(f"{i}. *{text}*\n")
                                else:
                                    content.append(f"{i}. {text}\n")
                    
                    # Recursively process other elements
                    elif child.name in ['div', 'article', 'section', 'main']:
                        process_content(child)

        # Start processing from body
        body = soup.find('body')
        if body:
            process_content(body)
            
        # Clean and combine content
        combined_text = '\n'.join(content)
        
        # Remove empty lines and excessive whitespace
        final_text = '\n'.join(
            line for line in combined_text.split('\n')
            if line.strip() and not any(skip in line.lower() for skip in [
                'footer', 'header', 'menu', 'navigation', 'sidebar',
                'copyright', '©', 'all rights reserved'
            ])
        )
        
        return {
            'status': 'success',
            'data': {
                'formatted_content': final_text,
                'title': soup.title.string.strip() if soup.title else '',
                'url': url
            }
        }
    
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }