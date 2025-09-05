import requests
import json

response = requests.get('https://api.nbrb.by/exrates/rates/dynamics/431?startDate=2025-01-01&endDate=2025-09-04')
data = response.json()
print(data)

# Сохранение в файл с правильным форматированием
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
