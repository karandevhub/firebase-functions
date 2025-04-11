# Rexx Cloud Python Functions

A collection of Firebase Cloud Functions for content processing and automation.

## Available Routes

### 1. Web Scraping Route

Extracts formatted content from web pages while preserving structure and emphasis.
#### Endpoint: `scrape`
#### Request Format
```json
{
    "url": "https://example.com/page-to-scrape"
}
```

#### Response Format
```json
{
    "status": "success",
    "data": {
        "formatted_content": "# Main Heading\nParagraph text\n*Important text*\n- List item\n1. Numbered item",
        "title": "Page Title",
        "url": "https://example.com/page-to-scrape"
    }
}
```

#### Content Formatting
- Headings are prefixed with `#` (level 1-6)
- Important text is wrapped in `*asterisks*`
- Unordered lists use `-` prefix
- Ordered lists use `1.` style numbering


## Setup & Deployment

1. Install dependencies:
```bash
cd functions
npm install
```

2. Deploy to Firebase:
```bash
firebase deploy --only functions
```

## Local Development

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run Firebase emulator:
```bash
firebase emulators:start
```