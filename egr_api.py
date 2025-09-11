import json
import pandas as pd
import requests as r
from datetime import datetime, timedelta
import time
import certifi


base_api_url = "https://egr.gov.by/api/v2/egr/getShortInfoByPeriod/{}/{}"
address_api_url = "https://egr.gov.by/api/v2/egr/getAddressByPeriod/{}/{}"
ved_api_url = "https://egr.gov.by/api/v2/egr/getVEDByPeriod/{}/{}"


def generate_periods(start_date, end_date, day_delta):
    periods = [(datetime(1900, 1, 1).date(), datetime(1990, 1, 1).date())]
    # periods = []
    day_delta = timedelta(days=day_delta)
    while start_date < end_date:
        if start_date+day_delta >= end_date:
            periods.append((start_date, end_date))
            break
        periods.append((start_date, start_date+day_delta))
        start_date += day_delta
    return periods


start_date = datetime(1990, 1, 1).date()
# end_date = datetime(2025, 9, 11).date()


index_date = 0
dates = generate_periods(start_date, datetime.now().date(), 20)
len_dates = len(dates)
data = []


while index_date < len_dates:
    start, end = dates[index_date]
    url = base_api_url.format(start.strftime("%d.%m.%Y"), end.strftime("%d.%m.%Y"))
    print(url)
    response = r.get(url, verify=certifi.where())
    if response.status_code != 200:
        print(f'Произошла ошибка на {url}. Ждем 5 сек и пробуем еще раз')
        time.sleep(5)
        continue

    for item in response.json():
        data.append(item)
    index_date += 1
    time.sleep(2)

print('Сбор данных по апи закончился')

with open('data_egr.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
