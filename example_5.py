# Редактирование и удаление данных
import pandas as pd

# Использование готового датасета
df = pd.read_csv("datasets/animal.csv")
print(df)

# Без удаления NaN, с заменой на значение 0
# df.fillna(0, inplace=True)
# print(df)

# С удалением NaN
df.dropna(inplace=True)
print(df)