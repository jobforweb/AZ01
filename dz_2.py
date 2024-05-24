# Определите среднюю зарплату (Salary) по городу (City) 
# - используйте файл приложенный к дз - dz.csv​
import pandas as pd

df = pd.read_csv("dz_datasets/dz.csv")
# print(df)

df.dropna(inplace=True)
print('=== Очищенный датасет: -----------')
print(df)

group = df.groupby("City")['Salary'].mean()
print('=== Cредняя зарплата по городу: -----------')
print(group)

