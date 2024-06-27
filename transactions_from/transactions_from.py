import pandas as pd

# Чтение данных из CSV-файла
df_csv = pd.read_csv('transactions.csv')
print("CSV file shape:", df_csv.shape)
print("CSV file head:")
print(df_csv.head())

# Чтение данных из XLSX-файла
df_xlsx = pd.read_excel('transactions_excel.xlsx')
print("XLSX file shape:", df_xlsx.shape)
print("XLSX file head:")
print(df_xlsx.head())
