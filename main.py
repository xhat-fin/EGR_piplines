import pandas as pd

with open('data.json', 'r') as file:
    data = file.read()


for item in list(data):
    print(item)
