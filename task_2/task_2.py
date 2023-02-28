import pandas as pd

# загрузка данных из csv файла в pandas DataFrame
df = pd.read_csv('показания.csv',sep=';')

# создание новой колонки 'Total' с суммой значений по месяцам
df['Total'] = df['Апрель'] + df['Май'] + df['Июнь']

# выборка данных только для общедомового счетчика (№ Квартиры == 0)
df_common = df[df['№ Квартиры'] == 0]

# выборка данных только для квартирных счетчиков (№ Квартиры > 0)
df_apartments = df[df['№ Квартиры'] > 0]

# группировка данных по номеру дома и суммирование значений Total
grouped_common = df_common.groupby('№ Дома')['Total'].sum()
grouped_apartments = df_apartments.groupby('№ Дома')['Total'].sum()

# проверка на равенство суммы по общедомовому счетчику и сумме по квартирным счетчикам
for house in grouped_common.index:
    if grouped_common[house] != grouped_apartments.get(house, 0):
        print('В доме №', house, 'возможно переданы неверные показания.')



# Дана таблица с показаниями счетчиков электроэнергии за 2 квартал (апрель, май, июнь) в файле "Показания.csv"
# В таблице строка, содержащая номер квартиры - относится к квартирному счетчику. Строка, где № квартиры равен 0 - к общедомовому.
# 2. Определить, в каком доме, возможно, переданы неверные показания.
# Критерий: сумма потребления по общедомовому счетчику за оба периода не равна сумме потребления за оба периода
# всех квартирных счетчиков этого дома.
