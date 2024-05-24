# Группировка по конкретным характеристикам
import pandas as pd

# Использование готового датасета
df = pd.read_csv("datasets/animal.csv")
print(df)

group = df.groupby("Пища")['Средняя продолжительность жизни'].mean()
print(group)