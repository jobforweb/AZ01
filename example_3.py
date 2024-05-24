
import pandas as pd

# Использование готового датасета
df = pd.read_csv("datasets/World-happiness-report-2024.csv")

print(df.head()) # Выводим первые 5 строки
# print(df.info()) # Выводим информацию о датасете
# print(df.describe()) # Выводим статистику

# print(df['Country name']) # Выводим один столбец
# print(df[['Country name','Regional indicator']]) # Выводим несколько столбцов

# print(df.loc[56]) # Вывод строки по индексу
# print(df.loc[56, 'Freedom to make life choices']) # Вывод значения определенного столбца по индексу

# print(df[df['Healthy life expectancy']>0.7]) # Условие выборки по значению столбца
