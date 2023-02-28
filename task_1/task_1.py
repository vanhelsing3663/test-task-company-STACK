import pandas as pd

meters_data = pd.read_csv('Показания.csv', sep=';')
electricity_consumption_apr_mai = meters_data['Май'] - meters_data['Апрель'] # потребление эл-и за апрель - май
electricity_consumption_jun_mai = meters_data['Июнь'] - meters_data['Май'] # потребление эл-и за май - июнь
meters_data['потребление за апрель-май'] = list(electricity_consumption_apr_mai)
meters_data['потребление за май-июнь'] = list(electricity_consumption_jun_mai)
print(meters_data)
meters_data.to_csv('Потребление.csv', mode='a', index=True, header=True)

# 1. Рассчитать потребление электроэнергии за период апрель-май и май-июнь для всех счетчиков (как разность
# соответствующих показаний).
# Сформировать новый файл "Потребление.csv", записать в него и исходные, и рассчитанные данные.