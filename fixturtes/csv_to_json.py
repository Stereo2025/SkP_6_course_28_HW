import csv
import json


def converter(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file):
            add_to_list = {'model': model,
                           'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            add_to_list['fields'] = row
            result.append(add_to_list)

    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json.dumps(result, ensure_ascii=False, indent=4))


converter('ads.csv', 'ads.json', 'ads.ads')
converter('categories.csv', 'categories.json', 'ads.categories')
converter('user.csv', 'user.json', 'user.user')
converter('location.csv', 'location.json', 'user.location')
