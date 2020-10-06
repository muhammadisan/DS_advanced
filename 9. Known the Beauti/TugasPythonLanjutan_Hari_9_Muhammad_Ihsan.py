from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://www1.gogoanime.movie/'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req)
data = BeautifulSoup(html, 'html.parser')

titles = data.findAll('p', 'name')
episodes = data.findAll('p', 'episode')

titles_clean = []
episodes_clean = []
for title in titles:
  x = str(title).split('>')
  titles_clean.append(x[2][0:-3])

for episode in episodes:
  x = str(episode).split('>')
  episodes_clean.append(x[1][0:-3])

import pandas as pd

df = pd.DataFrame({'Judul':titles_clean, 'Episode Terakhir':episodes_clean})

print(df)