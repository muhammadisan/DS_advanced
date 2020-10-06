import pandas as pd

df_indo = pd.read_json('indonesia.json')
df_south_korea = pd.read_json('south-korea.json')
df_vietnam = pd.read_json('vietnam.json')

df_indo_ = df_indo[(df_indo['Date'] >= '2020-07') & (df_indo['Date'] <= '2020-09-01')].reset_index()
df_south_korea_ = df_south_korea[(df_south_korea['Date'] >= '2020-07') & (df_south_korea['Date'] <= '2020-09-01')].reset_index()
df_vietnam_ = df_vietnam[(df_indo['Date'] >= '2020-07') & (df_vietnam['Date'] <= '2020-09-01')].reset_index()

import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(df_indo_.index, df_indo_['Confirmed'], label='Indonesia')
ax.plot(df_south_korea_.index, df_south_korea_['Confirmed'], label='South Korea')
ax.plot(df_vietnam_.index, df_vietnam_['Confirmed'], label='Vietnam')

ax.set_xticks([0, 30, 62])
ax.set_xticklabels(['1-Jul-2020', '1-Aug-2020', '1-Sep-2020'])
ax.set_ylabel('Confirmed', fontsize=15)
ax.set_xlabel('Date', fontsize=15)
ax.set_title('Coronavirus Cases per 1 Jul - 1 Sep 2020', fontsize=17)
ax.legend(fontsize=13)

plt.show()

# Indonesia memiliki confirmed cases tertinngi sepanjang 1 Juli - 1 September, dan mencapai 175K+ cases pada 1 September
# Convirmed cases Vietnam sangat rendah dibanding Indonesia, dalam skala yang ada terlihat sangat datar
# Korea Selatan mengalami kenaikan kasus di pertengahan bulan Agustus setelah sebelumnya cukup landai