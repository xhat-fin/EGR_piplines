import json
import requests as r
from datetime import datetime, timedelta
import time
import certifi


class PipeLine:
    def __init__(self, api, output_file_json):
        self.api = api
        self.output_file_json = output_file_json
        self.periods = []

    def generate_periods(self, start_date, end_date, day_delta):
        periods = [(datetime(1900, 1, 1).date(), datetime(1990, 1, 1).date())]
        day_delta = timedelta(days=day_delta)
        while start_date < end_date:
            if start_date + day_delta >= end_date:
                periods.append((start_date, end_date))
                break
            periods.append((start_date, start_date + day_delta))
            start_date += day_delta

        self.periods = periods
        return periods

    def get_info_by_periods(self, start_date, end_date, day_delta):
        periods = self.generate_periods(start_date, end_date, day_delta)
        index_date = 0
        len_dates = len(periods)
        data = []

        while index_date < len_dates:
            # получаем даты для подставления в АПИ
            start, end = periods[index_date]

            # формируем апи строку
            api_url = self.api.format(start.strftime("%d.%m.%Y"), end.strftime("%d.%m.%Y"))
            print(api_url)

            try:
                # делаем апи запрос
                response = r.get(api_url, verify=certifi.where(), timeout=60)

                # если запрос неуспешный, то пробуем еще раз через 5 секунд
                if response.status_code != 200:
                    print(f'Произошла ошибка {response.status_code} на {api_url}. Ждем 5 сек и пробуем еще раз')
                    time.sleep(5)
                    continue

                # итерируемся по полученным данным и кладем их в основную переменную
                for item in response.json():
                    data.append(item)

                # инкрементируем индекс для следующей даты
                index_date += 1
                time.sleep(2)

            except Exception as e:
                print(f'Ошибка: {e}. Ждем 5 сек и пробуем еще раз')
                time.sleep(5)

        print(f'Сбор данных по {self.output_file_json} закончился')

        with open(self.output_file_json, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Файл {self.output_file_json} сформирован")

    def __str__(self):
        return f'{self.periods}'

short_info_api_url = "https://egr.gov.by/api/v2/egr/getShortInfoByPeriod/{}/{}"
address_api_url = "https://egr.gov.by/api/v2/egr/getAddressByPeriod/{}/{}"
ved_api_url = "https://egr.gov.by/api/v2/egr/getVEDByPeriod/{}/{}"


short_info = PipeLine(short_info_api_url, 'short_info.json')
address_info = PipeLine(short_info_api_url, 'address_info.json')
ved_info = PipeLine(short_info_api_url, 'ved_info.json')

start_date = datetime(2025, 1, 1).date()
end_date = datetime.now().date()
