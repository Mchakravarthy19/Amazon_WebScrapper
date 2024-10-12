import requests
from bs4 import BeautifulSoup
from skimage.io import imread 
import matplotlib.pyplot as plt


url = input("Enter the product url: ")
response = requests.get(url)


from selenium import webdriver
driver = webdriver.Chrome()  
driver.get(url)


html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

try: 
    product_name = soup.find('span', {'id': 'productTitle'}).text.strip()
except Exception as e:
    product_name = "Product title not found"

try:
    price = soup.find('span', {'class': "a-price-whole"}).text.strip()
except Exception as e:
    price = "Product price not found"
try:
    rating = soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip() 
except Exception as e:
    rating = "Reviews not found"


print(f"Product Name: {product_name}")
print(f"Price: {price}")
print(f"Rating: {rating}")

try:
    img = soup.find('img', {'id': 'landingImage'})
    image_url = img['src']
    image = imread(image_url)
    plt.imshow(image)
    plt.title("Product Image")
    plt.axis(False)
    plt.show()

except Exception as e:
    print("Image not found")