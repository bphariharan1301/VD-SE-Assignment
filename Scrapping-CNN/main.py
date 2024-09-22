import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    # Found that the titles of articles are in span and h2 tags with below mentioned classes alone in the webpage
    article_spans = soup.find_all("span", class_="container__headline-text")
    article_h2s = soup.find_all("h2", class_="container__title_url-text")
    articles = article_spans + article_h2s

    print(f"Found {len(articles)} articles on CNN website")
    with open("cnn_headlines.txt", "w") as file:
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article.get_text()}")
            file.write(f"{i}. {article.get_text()}\n")
    print("Headlines saved to cnn_headlines.txt")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
