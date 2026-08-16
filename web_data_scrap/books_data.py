# Web Scraping - Books

import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/page-1.html"

books = []

for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select("article.product_pod")

    for item in items:

        title = item.h3.a.get("title")
        price = item.select_one(".price_color").get_text(strip=True)
        stock = item.select_one(".availability").get_text(" ", strip=True)

        rating = item.select_one("p.star-rating")
        rating = rating.get("class")[1] if rating else "Unknown"

        link = item.h3.a.get("href")

        books.append({
            "title": title,
            "price": price,
            "availability": stock,
            "rating": rating,
            "link": link
        })

with open("books_data.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "title",
            "price",
            "availability",
            "rating",
            "link"
        ]
    )

    writer.writeheader()
    writer.writerows(books)

print("Books collected:", len(books))

for book in books[:10]:
    print(book)