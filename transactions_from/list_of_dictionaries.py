import re
from typing import Dict, List

import pandas as pd


def read_csv(file_path: str) -> List[Dict]:
    """
    Читает CSV-файл и возвращает список транзакций в виде словарей.
    """
    df = pd.read_csv(file_path)
    transactions = df.to_dict(orient="records")
    return transactions


def read_xlsx(file_path: str) -> List[Dict]:
    """
    Читает XLSX-файл и возвращает список транзакций в виде словарей.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient="records")
    return transactions


def search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет транзакции с указанной поисковой строкой в описании.
    """
    pattern = re.compile(search_str, re.IGNORECASE)
    result = [transaction for transaction in transactions if pattern.search(str(transaction.get("description", "")))]
    return result


if __name__ == "__main__":
    # Пример использования

    # Чтение данных из CSV файла
    csv_file_path = "transactions.csv"
    csv_transactions = read_csv(csv_file_path)
    print("CSV Transactions:")
    print(csv_transactions[:5])  # Вывод первых 5 транзакций для наглядности

    # Чтение данных из XLSX файла
    xlsx_file_path = "transactions_excel.xlsx"
    xlsx_transactions = read_xlsx(xlsx_file_path)
    print("XLSX Transactions:")
    print(xlsx_transactions[:5])  # Вывод первых 5 транзакций для наглядности

    # Поиск транзакций с определенной строкой в описании
    search_term = "покупка"
    filtered_transactions = search_transactions(csv_transactions + xlsx_transactions, search_term)
    print(f"Filtered Transactions by '{search_term}':")
    print(
        filtered_transactions[:5]
    )  # Вывод первых 5 найденных транзакций для наглядностиых 5 найденных транзакций для наглядности
