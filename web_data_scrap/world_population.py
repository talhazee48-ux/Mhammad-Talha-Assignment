# Web Scraping - World Population

import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=15
)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wikitable")

population_data = []

if table:

    rows = table.find_all("tr")

    for row in rows[1:]:

        cells = row.find_all(["td", "th"])

        if len(cells) >= 4:

            values = [
                cell.get_text(" ", strip=True)
                for cell in cells
            ]

            population_data.append({
                "rank": values[0],
                "country": values[1],
                "population": values[2],
                "percent_world": values[3]
            })

with open(
    "world_population.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "rank",
            "country",
            "population",
            "percent_world"
        ]
    )

    writer.writeheader()
    writer.writerows(population_data)

print("Countries collected:", len(population_data))

for country in population_data[:15]:
    print(country)