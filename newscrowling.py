import requests
from bs4 import BeautifulSoup
import pandas as pd
keyword = input()
url = f'https://search.naver.com/search.naver?where=news&query={keyword}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('a[data-heatmap-target=".tit"]')
# print(articles)
article = articles[0]
title = article.text
# print(title)
title_tot = pd.DataFrame([article.text for article in articles], columns=['title'])
print(title_tot.head())
