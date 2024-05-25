def list_dictionary(list_dict: list, state: str = "EXECUTED") -> list:
    """ Функцию, которая принимает на вход список словарей
     и значение для ключа state """
    filtred_list = []
    for ld in list_dict:
        if ld.get("state"):
            filtred_list.append(ld)
    return filtred_list


def list_sorted_date(list_dict: list, direction: bool = True) -> list:
    """ Функция сортирует словари по дате """
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
