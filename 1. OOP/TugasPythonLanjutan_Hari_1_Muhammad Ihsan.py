#1 Bahasa utama saya untuk mengerjakan project Data Science (Shopee code league, Sanbercode data science dasar).
# Terkadang untuk competitive programming selain bahasa C++. Python bisa digunakan untuk big number dengan mudah.

#2 NLP, Deep Learning. Mungkin bisa dibuat 2 bulan

3#
class manipulasi:
  def __init__(self, data):
    self.capitalize = data.capitalize()
    self.lower = data.lower()
    self.upper = data.upper()
    self.split = data.split()

data = 'saya tinggal di Indonesia'
data1 = manipulasi(data)

print('data = ', data)
for val in data1.__dict__.values():
  print(val)