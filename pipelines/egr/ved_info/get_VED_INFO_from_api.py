from egr_api import PipeLineEGRbyPeriod
from datetime import datetime


# API
ved_api_url = "https://egr.gov.by/api/v2/egr/getVEDByPeriod/{}/{}"

# Наследуемся от пайплайна
ved_info = PipeLineEGRbyPeriod(ved_api_url, 'ved_info.json')

# устанавливаем значения дат для апи
start_date = datetime(1990, 1, 1).date()
end_date = datetime.now().date()
default_date = (datetime(1900, 1, 1).date(), datetime(1990, 1, 1).date())

# запускаем шарманку
ved_info.get_info_by_periods(start_date=start_date, end_date=end_date, day_delta=180, default_date=default_date)
