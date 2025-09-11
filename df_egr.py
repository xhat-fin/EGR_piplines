import pandas as pd
import json

path_file = 'data_egr.json'

df = pd.read_json(path_file)
print(df.info())
print(df.describe())
print(df.head())
print(df.head().T)




# with open(path_file, 'r', encoding='utf-8') as f:
#     content = f.read()
#
# content = content.replace('[', '')
# content = content.replace(']', '')
# content = "[" + content + "]"
#
# content = json.loads(content)
#
# with open('data_egr_v2.json', 'w', encoding='utf-8') as file:
#     json.dump(content, file, ensure_ascii=False, indent=4)
