# Web Scraping - Technology News

import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

news = []

stories = soup.select("tr.athing")

for story in stories:

    title_tag = story.select_one("span.titleline a")

    if not title_tag:
        continue

    title = title_tag.get_text(" ", strip=True)
    link = title_tag.get("href")

    details = story.find_next_sibling("tr")

    points = "0"
    comments = "0"

    if details:

        score = details.select_one("span.score")

        if score:
            points = score.get_text(strip=True)

        links = details.select("a")

        for link_tag in links:

            text = link_tag.get_text(" ", strip=True)

            if "comment" in text:
                comments = text.split()[0]

    news.append({
        "title": title,
        "url": link,
        "points": points,
        "comments": comments
    })

with open("technology_news.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "title",
            "url",
            "points",
            "comments"
        ]
    )

    writer.writeheader()
    writer.writerows(news)

print("News collected:", len(news))

for item in news[:10]:
    print(item)