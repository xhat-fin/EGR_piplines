import pandas as pd

df = pd.read_json('data.json')
day_max_cur = df.loc[df['Cur_OfficialRate'].idxmax()]

print(day_max_cur)
