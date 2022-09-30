import pandas as pd
from openpyxl import Workbook
import xlrd

df=pd.read_excel("../Data/testdata.xlsx","emp")
wb=Workbook("../Data/testdata.xlsx","emp")
ws=wb.active
n=ws.rows

# print(df)
# df.to_excel("../Data/newcopy.xlsx","emp1")
# print(df.columns)
# col_value = df["Emp_ID"]
# print(col_value)
# row_value = df["Name"]
# print(row_value)

# first_col_value = df["Emp_ID"][0]
# print(first_col_value)
# first_row_value = df["Name"][0]
# print(first_row_value)

rows_value = df.head(1)
print(rows_value)
print(len(rows_value))








