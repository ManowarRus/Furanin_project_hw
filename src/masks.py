def get_mask_cards(numbers: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
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
    result = "**" + numbers1[-4:]
    return result
