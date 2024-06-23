import json
import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


def transaction_amount(file_path: str) -> list:
    """Функция, которая выводит сумму транзакции"""
    try:
        logger.info(f"Открытие json файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        logger.info(f"Проверяем, чыто файл {file_path} не пустой")
        if isinstance(repos, list):
            return repos
        else:
            logger.info(f"Возвращаем пустой словарь, если файл {file_path} пустой")
            return []

    except Exception as e:
        print(f"Ошибка {e}")
        return []
