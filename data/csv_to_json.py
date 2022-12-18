import csv
import json


# Functions

def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model,
                      'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'location_id' in row:
                row['locations'] = [int(row['location_id'])]
                del row['location_id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as jf:
        jf.write(json.dumps(result, ensure_ascii=False, indent=2))


convert_file(f"ad.csv", f"ads.json", 'ads.urls')
convert_file(f"category.csv", f"categories.json", 'ads.category')
convert_file(f"user.csv", f"user.json", 'users.user')
convert_file(f"location.csv", f"location.json", 'users.location')
