from urllib.request import urlopen
from bs4 import BeautifulSoup

alamat = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

table = data.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

hasil = []
for row in rows:
  info = []
  for cell in row.findAll(["td", "th"]):
    info.append(cell.get_text())
    hasil.append(info)

hasil_unique = []
for x in hasil:
  if x not in hasil_unique:
    hasil_unique.append(x)

hasil_unique_clean = []
for x in hasil_unique:
  temp = []
  for s in x:
    s = s.replace('\n', '')
    temp.append(s)
  hasil_unique_clean.append(temp)

import pandas as pd

def data_frame(lst):
  df = pd.DataFrame(lst[1:], columns=lst[0]).set_index('Rank')
  display(df)

def df_to_excel(lst):
  df = pd.DataFrame(lst[1:], columns=lst[0]).set_index('Rank')
  df.to_excel('muhammadisan2015.xlsx')

data_frame(hasil_unique_clean)
df_to_excel(hasil_unique_clean)