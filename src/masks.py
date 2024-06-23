import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_cards(numbers: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""

    logger.info(f"Задаём формат маски для номера банковской карты {numbers}")

    result = ""
    number_list = list(numbers)
    for i, num in enumerate(number_list):
        if i == 3 or i == 7 or i == 11:
            result += num + " "
        else:
            result += num
    result1 = result[0:7] + "** ****" + result[14:]
    return result1


def get_mask_bank_account(numbers1: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""

    logger.info(f"Проверяем правильность написания {numbers1}")

    result = "**" + numbers1[-4:]
    return result
