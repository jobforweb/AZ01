
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
    }
# Структура Dataframe из pandas
df = pd.DataFrame(data)
print(df)
