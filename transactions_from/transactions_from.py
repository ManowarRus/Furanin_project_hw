import pandas as pd


def read_csv(file_path: str) -> list:
    """Читает CSV-файл и возвращает список транзакций в виде словарей."""
    # Чтение данных из CSV файла в DataFrame
    df = pd.read_csv(file_path)

    # Преобразование DataFrame в список словарей
    transactions = df.to_dict(orient="records")

    return transactions


def read_xlsx(file_path: str) -> list:
    """Читает XLSX-файл и возвращает список транзакций в виде словарей."""
    # Чтение данных из XLSX файла в DataFrame
    df = pd.read_excel(file_path)

    # Преобразование DataFrame в список словарей
    transactions = df.to_dict(orient="records")

    return transactions



if __name__ == "__main__":
    # Пример использования

    # Путь к CSV файлу
    csv_file_path = "transactions.csv"
    csv_transactions = read_csv(csv_file_path)
    print("CSV Transactions:")
    print(csv_transactions[:5])  # Вывод первых 5 транзакций для наглядности

    # Путь к XLSX файлу
    xlsx_file_path = "transactions_excel.xlsx"
    xlsx_transactions = read_xlsx(xlsx_file_path)
    print("XLSX Transactions:")
    print(xlsx_transactions[:5])  # Вывод первых 5 транзакций для наглядности
