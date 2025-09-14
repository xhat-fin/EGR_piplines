import requests as r
from datetime import datetime, timedelta
import time
import certifi
import pandas as pd
import json


class PipeLineEGRbyPeriod:
    def __init__(self, api, output_file_json):
        self.api = api
        self.output_file_json = output_file_json
        self.periods = []

    def generate_periods(self, start_date, end_date, day_delta, default_date):
        # default_date : (datetime(1900, 1, 1).date(), datetime(1990, 1, 1).date())
        periods = []
        if default_date:
            periods.append(default_date)

        day_delta = timedelta(days=day_delta)
        while start_date < end_date:
            if start_date + day_delta >= end_date:
                periods.append((start_date, end_date))
                break
            periods.append((start_date, start_date + day_delta))
            start_date += day_delta

        self.periods = periods
        return periods

    def get_info_by_periods(self, start_date, end_date, day_delta, default_date):
        now_date = datetime.now()
        periods = self.generate_periods(start_date, end_date, day_delta, default_date)
        index_date = 0
        len_dates = len(periods)
        data = []

        while index_date < len_dates:
            # получаем даты для подставления в АПИ
            start, end = periods[index_date]

            # формируем апи строку
            api_url = self.api.format(start.strftime("%d.%m.%Y"), end.strftime("%d.%m.%Y"))
            print(f'Индекс даты: {index_date}. API: {api_url}')

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
        df = pd.json_normalize(data)
        df = df.drop_duplicates()
        df.to_json(self.output_file_json,
                   orient='records',
                   force_ascii=False,
                   indent=4,
                   index=False)
        print(f"Файл {self.output_file_json} сформирован. Затрачено времени: {datetime.now() - now_date}")

    def __str__(self):
        return f'{self.periods}'
