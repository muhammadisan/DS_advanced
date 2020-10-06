import pandas as pd

df = pd.read_csv('INDODAPOERData.csv')

tahun = [str(x) for x in range(2001,2012)]
kota = ['Bandung, Kota', 'Bandung Barat, Kab.', 'Bandung, Kab.', 'Cimahi, Kota']
df_gdp = df[df['Indicator Code'] == 'NA.GDP.EXC.OG.CR'][['Country Name'] + tahun].set_index('Country Name')
df_gdp_clean = df_gdp.loc[kota]

import matplotlib.pyplot as plt

plt.style.use('ggplot')

marker = ['.', '*', 'p', 'v']
i = 0
for city in df_gdp_clean.index:
    plt.plot(range(11), df_gdp_clean.loc[city], label=city, marker=marker[i])
    i += 1

plt.xticks(range(11), tahun)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('GDP')
plt.title('GDP tanpa minyak dan gas')
plt.show()