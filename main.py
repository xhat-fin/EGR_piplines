import pandas as pd

df = pd.read_json('data.json')

# перевод dataframe в xlsx
# df.to_excel('cur.xlsx', index=False)

# print(df.head(n=1)) # смотрит указанное кол-во первых строк
# print(df.tail(n=1)) # смотрит указанное кол-во последних строк

# print(df.describe()) # Статистика по датафрейму
# print(df.describe(include=[float])) # статистика по указанному типу данных
# print(df.describe(exclude=[int])) # исключаем определенный тип данных

"""
транспонируем таблицу с статистикой и получаем столбцы с характеристик и строки названия столбцов
Думаю так можно транспонировать любой датафрейм
"""
# print(df.describe().T)
# print(df.head(n=3).T)

"""
Информация по столбцам, сколько пропущенных значений NULL, какие типы данных в столбцах и всякое разное
"""
#
# print(df.info(show_counts=True, memory_usage=True))
# print(df.info(verbose=True))
# print(df.info())


"""
Возвращает кортеж (строка, столбец). Количество строк и столбцов.
"""
# print(df.shape)


"""
Возвращает Объект Индекс с названиями столбцов. 
Можно преобразовать в список с помощью list()
"""
# print(df.columns)
# print(list(df.columns))



"""
Количество пропущенных значений
"""
# print(df.isnull()) # датафрейм где Тру и False это налловое значение или нет
# print(df.isnull().sum())
# print(df.isnull().sum().sum())


"""
Выделить конкретный столбец с данными. В пандас это называется Series
"""
# print(df['Cur_OfficialRate'])
# print(df[['Cur_OfficialRate', 'Date']])



"""
вернуть конкретную строку
вернуть диапазон строк
"""
# print(df[df.index==1])
# print(df[df.index.isin([1, 3, 10, 123])])


"""
loc
iloc
получение определенных строк
"""

print(df.loc[1])
print()
print(df.iloc[1])
