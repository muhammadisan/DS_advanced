import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
import csv

data_penduduk = pd.read_csv('jumlah-penduduk-kota-bandung.csv')
data_penduduk.sort_values(['Kecamatan'], inplace=True, ignore_index=True)
data_luas = pd.read_csv('luas-wilayah-menurut-kecamatan-di-kota-bandung-2017.csv')

dct = {}
dct['Nama Kecamatan'] = []
dct['Kepadatan Penduduk'] = []

for i in range(len(data_luas.index)):
    dct['Nama Kecamatan'].append(data_penduduk.iloc[i,0])
    dct['Kepadatan Penduduk'].append(data_penduduk.iloc[i,2]/data_luas.iloc[i,1] * 100)

df = pd.DataFrame(dct)
df.to_csv('Kepadatan Penduduk.csv', index=False)

wb = Workbook(write_only=True)
ws = wb.create_sheet()

data = open('Kepadatan Penduduk.csv')
rows = csv.reader(data, delimiter=',')

index = 0
for row in rows:
    data_clean = []
    for i in row:
        try:
            i = float(i)
        except:
            pass
        data_clean.append(i)
    row = data_clean
    ws.append(row)
    index +=1
len_row = len(row)

bar = BarChart()
bar.type = 'col'
bar.style = 3
bar.title = 'Kepadatan Penduduk'
bar.y_axis.title = 'Kepadatan per 100m2'
bar.x_axis.title = 'Kecamatan'

data = Reference(ws, min_col=2, min_row=1, max_row=index, max_col=len_row)
cats = Reference(ws, min_col=1, min_row=2, max_row=index)
bar.height = 10
bar.width = 30
bar.add_data(data, titles_from_data=True)
bar.set_categories(cats)
ws.add_chart(bar, "E2")

wb.save('Muhammad_Ihsan.xlsx')