# Amazon Product Web Scraper

This is a Python-based web scraper designed to retrieve key information from Amazon product pages. By providing a product URL, the scraper extracts details such as the product name, reviews, ratings, price, and image.

## Features

- Scrapes the following product details:
  - Product Name
  - Reviews
  - Ratings
  - Price
  - Product Image
- Utilizes the following libraries:
  - `BeautifulSoup4` for parsing HTML content
  - `requests` for making HTTP requests
  - `selenium` for interacting with dynamic content
- Simple and customizable for use in other scraping projects.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amazon-product-scraper.git
   cd amazon-product-scraper



2. Install the required dependencies:

```bash
pip install -r requirements.txt

```

    
## Usage/Examples
1. Run the scraper by providing the Amazon product URL as input:
```python

python scraper.py "https://www.amazon.com/dp/productID"

```
2. Scrapes the following product details:
  - Product Name
  - Reviews
  - Ratings
  - Price
  - Product Image

## EXAMPLE OUTPUT
```
Product Name: Example Product
Price: $29.99
Rating: 4.5 out of 5 stars
Reviews: 1500
Image URL: https://example.com/image.jpg
```


 




## REQUIREMENTS
 Scrapes the following product details:
  - Python 3.x
  - BeautifulSoup4
  - requests
  - selenium
