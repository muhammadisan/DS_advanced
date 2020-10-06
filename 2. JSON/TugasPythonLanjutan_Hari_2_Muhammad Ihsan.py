import json
import csv
import pandas as pd

class tugas_json:
    def csv_to_json(self):
        csvf = open('pulau_indonesia.csv')
        csv_reader = csv.reader(csvf, delimiter=',')
        next(csvf, None)

        data_list = []
        for rows in csv_reader:
            row = {}
            row['nama provinsi'] = rows[1]
            row['detail'] = {
                'bernama': rows[2],
                'tak bernama': rows[3],
                'total': rows[4]
            }
            data_list.append(row)

        jsonFilePath = 'Muhammad_Ihsan.json'
        jsonf = open(jsonFilePath, 'w')
        jsonf.write(json.dumps(data_list, indent=2))
    
    def json_to_pandas(self):
        df = pd.read_json('country_full.json')
        df.columns = ['Nama', 'Slug', 'ISO']
        return print(df)

tugas = tugas_json()
tugas.csv_to_json()
tugas.json_to_pandas()