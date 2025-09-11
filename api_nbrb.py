import requests
import json

response = requests.get('https://api.nbrb.by/exrates/rates/dynamics/431?startDate=2024-09-06&endDate=2025-09-05')
data = response.json()

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
