#muhammadisan2015

import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('https://pokemondb.net/pokedex/all')
data = BeautifulSoup(html.content, 'html5lib')
table = data.findAll('tr')

clean = []
for row in table:
  list_row = []
  for cell in row.find_all(['th', 'td']):
    text = cell.get_text()
    try:
      text = int(text)
    except:
      pass
    list_row.append(text)
  if list_row[0] == 501: break
  clean.append(list_row)

df = pd.DataFrame(clean[1:], columns=clean[0]).set_index('#')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics 
from scipy.spatial.distance import cdist 

x = df.drop(['Name', 'Type'], axis=1)
x_array = np.array(x)
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

distortions = [] 
inertias = [] 
mapping1 = {} 
mapping2 = {} 
K = range(1,10) 
  
for k in K: 
    kmeanModel = KMeans(n_clusters=k).fit(x_scaled) 
    kmeanModel.fit(x_scaled)     
      
    distortions.append(sum(np.min(cdist(x_scaled, kmeanModel.cluster_centers_, 'euclidean'),axis=1)) / x_scaled.shape[0]) 
    inertias.append(kmeanModel.inertia_) 
  
    mapping1[k] = sum(np.min(cdist(x_scaled, kmeanModel.cluster_centers_, 'euclidean'),axis=1)) / x_scaled.shape[0] 
    mapping2[k] = kmeanModel.inertia_

plt.plot(K, distortions, 'bx-') 
plt.xlabel('Values of K') 
plt.ylabel('Distortion') 
plt.title('The Elbow Method using Distortion') 
plt.show()

from sklearn.metrics import silhouette_score

data = []
k_list = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters = k).fit(x_scaled)
    labels = kmeans.labels_
    data.append(silhouette_score(x_scaled, labels, metric = 'euclidean'))
    k_list.append(k)

plt.plot(k_list,data)
plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(x_scaled)

df['Cluster'] = kmeans.labels_
df.to_csv('muhammadisan2015.csv')
print('nilai K terbaik adalah ', 2)