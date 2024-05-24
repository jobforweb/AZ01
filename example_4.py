# Добавление и удаление столбцов и строк с помощью функций Pandas
import pandas as pd

# Использование готового датасета
df = pd.read_csv("datasets/hh.csv")

# Добавляем столбец 
df['Test'] = [new for new in range(len(df))] # len(df) - количество строк в датасете .. 29 строк
print(df)

# Удаляем столбец 
df.drop('Test', axis=1, inplace=True) # axis=1 - удаляем столбец, axis=0 - удаляем строку , inplace=True - перезаписываем столбец
print(df)

# Удаляем столбец 
df.drop(28, axis=0, inplace=True)
print(df)