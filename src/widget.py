from src.masks import get_mask_bank_account, get_mask_cards


def get_masks_bank_accounts_cards(strings_number: str) -> str:
    """Функция приинимает на вход строку с информацией — тип карты/счета и номер карты/счета и
    возвращает исходную строку с замаскированным номером карты/счета."""
    if "Visa" in strings_number or "Maestro" in strings_number or "MasterCard" in strings_number:
        word_list = strings_number.split()
        num_list = []
        symbol_list = []
        for word in word_list:
            if word.isnumeric():
                num_list.append(word)
            elif word.isalpha():
                symbol_list.append(word)
        num_list1 = "".join(num_list)
        symbol_list1 = " ".join(symbol_list)
        result = get_mask_cards(num_list1)
        return f"{symbol_list1} {result}"
    else:
        word_list = strings_number.split()
        num_list = []
        symbol_list = []
        for word in word_list:
            if word.isnumeric():
                num_list.append(word)
            elif word.isalpha():
                symbol_list.append(word)
        num_list1 = "".join(num_list)
        symbol_list1 = " ".join(symbol_list)
        result = get_mask_bank_account(num_list1)
        return f"{symbol_list1} {result}"


def convert_date(data_string: str) -> str:
    """функция, которая принимает на вход строку даты и время вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018"""
    data_result = data_string[:10]
    data_list = data_result.split("-")
    data_list.reverse()
    result = "-".join(data_list)
    return result
