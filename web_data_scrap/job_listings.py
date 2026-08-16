# Web Scraping - Job Listings

import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

cards = soup.select("div.card-content")

for card in cards:

    title = card.select_one("h2.title")
    company = card.select_one("h3.company")
    location = card.select_one("p.location")

    if title and company and location:

        title = title.get_text(" ", strip=True)
        company = company.get_text(" ", strip=True)
        location = location.get_text(" ", strip=True)

        link_tag = card.select_one("a.card-footer-item")
        link = link_tag.get("href") if link_tag else ""

        jobs.append({
            "job_title": title,
            "company": company,
            "location": location,
            "url": link
        })

with open("job_listings.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "job_title",
            "company",
            "location",
            "url"
        ]
    )

    writer.writeheader()
    writer.writerows(jobs)

print("Jobs collected:", len(jobs))

for job in jobs[:10]:
    print(job)