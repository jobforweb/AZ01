
import pandas as pd

print('=== Football Player Statistics: -------------------------------')

df = pd.read_csv("dz_datasets/players_3120.csv")

print(df.head()) # Выводим первые 5 строки

print(df.describe()) # Выводим статистику

print(df.info()) # Выводим информацию о датасете