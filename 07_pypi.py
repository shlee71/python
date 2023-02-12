import pandas

house = pandas.read_csv('house.csv')
print(house)
print('='*110)
print(house.head(2))
print('='*110)
print(house.describe())
print('='*110)
print(house.tail(1))