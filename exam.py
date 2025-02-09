# Task 1
# import numpy as np

# arr = np.random.randint(0 ,10, 10)
# print(arr.mean())
# print(np.median(arr))
# print(arr.std())



# Task 2
# def multiplication_table(num: int):
#     res_list = []
#     for i in range(1, num+1):
#         res_list.append(f'{i} x {num} = {i*num}')
#     return res_list

# print(multiplication_table(7))

# Task 3
# class Date:
#     def __init__(self, month, day, year):
#         if not (month >=1 and month <= 12):
#             raise ValueError("Month range is between 1 and 12 ONLY")
#         if not (day >=1 and month <= 31):
#             raise ValueError("Day range is between 1 and 31 ONLY")
        

#         self.month = month
#         self.day = day
#         self.year = year


#     def birinchi_format(self):
#         # MM/DD/YYYY
#         return f"{self.month}/{self.day}/{self.year}"
    
#     def ikkinchi_format(self):
#         # Month day, year
#         months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#                   'August', 'September', 'October', 'November', 'December']
#         return f"{months[self.month - 1]} {self.day}, {self.year}"

#     def uchinchi_format(self):
#         # day month year
#         months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#                   'August', 'September', 'October', 'November', 'December']
#         return f"{self.day} {months[self.month - 1]} {self.year}"

# data = Date(8, 3, 2006)
# print(data.birinchi_format())
# print(data.ikkinchi_format())
# print(data.uchinchi_format())

# Task 4
# import csv

# with open('TestMax.csv', 'r') as file:
#     reader = csv.reader(file)
#     reader.__next__()
#     for row in reader:
#         print(max(row[2:]))

import pandas as pd

df = pd.read_csv('TestMax.csv')
df['MaxValue'] = df[['Max1', 'Max2', 'Max3']].max(axis=1)
# print(df['MaxValue'])

print(df[['Year1', 'MaxValue']])
