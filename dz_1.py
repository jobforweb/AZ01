# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# - Загрузите набор данных из CSV-файла в DataFrame.
# - Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# - Выведите информацию о данных (.info()) и статистическое описание (.describe()).
import pandas as pd

print('=== Football Player Statistics: -------------------------------')

df = pd.read_csv("dz_datasets/players_3120.csv")

print(df.head()) # Выводим первые 5 строки

print(df.describe()) # Выводим статистику

print(df.info()) # Выводим информацию о датасете