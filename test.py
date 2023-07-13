import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.styles import Font
#['2020', '2021', '2022', '2023']
df = pd.concat(pd.read_excel(r'C:\Users\НиколаевПА\PycharmProjects\ProjectsBot\Projects.xlsx', engine='openpyxl',
                   sheet_name=None), ignore_index=True)
n = '20-007'
num = df[(df['Наименование'].str.contains(n, na=False)) | (df['Шифр объекта'].str.contains(n, na=False))]
print(num[['Наименование', 'Шифр объекта', 'Наличие в архиве']])

#num = np.column_stack([sheet[col].astype(str).str.contains(n) for col in sheet])
#num = df[df.isin([n]).any(axis=1)]
#sheet = pd.read_excel(io='test.xlsx', engine='openpyxl')