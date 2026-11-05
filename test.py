import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for q in soup.find_all("div", class_="quote"):
    text = q.find("span", class_="text").text
    print("👉", text)