import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import csv


base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
#page = urllib3.urlopen(base_url)
params = {
    "k": "bags",
    "crid": "2M096C61O4MLT",
    "qid": "1653308124",
    "sprefix": "ba,aps,283",
    "ref": "sr_pg_1"
}
header=({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def scrape_product_listings(url, headers, num_pages=20):
    data = []

    for page in range(1, num_pages + 1):
        params["page"] = page
        response = requests.get(url, params=params, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.find_all("div", class_="s-result-item")
        print(products)

        for product in products:
            product_url = product.find("a", class_="a-link-normal")["href"]
            product_name = product.find("span", class_="a-text-normal").text.strip()
            product_price = product.find("span", class_="a-price").find("span", class_="a-offscreen").text.strip()
            rating = product.find("span", class_="a-icon-alt").text.split()[0]
            num_reviews = product.find("span", {"aria-label": "ratings"}).text.split()[0]

            data.append({
                "Product URL": product_url,
                "Product Name": product_name,
                "Product Price": product_price,
                "Rating": rating,
                "Number of Reviews": num_reviews
            })
          
    return data


#product_data = scrape_product_listings(base_url, header)
df = pd.DataFrame()

def scrape_product_details(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Add code to scrape ASIN, Product Description, Manufacturer, etc.

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer
    }


def scrape_product_details(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Add code to scrape ASIN, Product Description, Manufacturer, etc.

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer
    }

csv_filename = "amazon_products.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['url', 'name', 'price', 'rating', 'reviews', 'description', 'asin', 'product_description', 'manufacturer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
df = pd.read_csv("amazon_products.csv")

df.shape

df.head(10)

df.tail(10)
