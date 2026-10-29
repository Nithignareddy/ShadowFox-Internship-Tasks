import requests
from bs4 import BeautifulSoup

url = "https://www.kluniversity.in/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.text.strip())