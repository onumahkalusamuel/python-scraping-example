import requests
from bs4 import BeautifulSoup
import csv

# scraping target
URL = "https://www.allcot.com/en/portfolio-proyects/"
page = requests.get(URL)

# open file for writing
csv_file = open('proyects.csv', 'w')
writer = csv.writer(csv_file)

# write the headers
writer.writerow(['Name', 'Country', 'Links'])

# parse html
soup = BeautifulSoup(page.content, "html.parser")

# pick all portfolio posts
proyects = soup.find_all("div", class_="portfolio-post")

# loop through, clean up and insert to csv
for proyect in proyects:
    title = proyect.find("h5", class_="portfolio-bottom-caption-title")
    link = title.find("a")
    country = proyect.find("ul", class_="portfolio-bottom-caption-category")
    
    writer.writerow([title.text.strip(), country.text.strip(), link["href"]])

# close the file stream
csv_file.close()