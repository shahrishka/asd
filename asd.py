import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

for unique_value in data['whoAmI'].unique():
    data[unique_value] = data['whoAmI'].apply(lambda x: 1 if x == unique_value else 0)

data.head()