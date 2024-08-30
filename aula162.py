# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
# from pytz import timezone

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1724975976.02707))

# print()
# data = datetime.now(timezone('Asia/Tokyo'))
# print(data)
# print()


# data_str_data = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y' 



# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)