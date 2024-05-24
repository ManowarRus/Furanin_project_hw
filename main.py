from src.widget import convert_date, get_masks_bank_accounts_cards

card_check_number = str(input("Введите номер карты или счет: "))
print(get_masks_bank_accounts_cards(card_check_number))

date_number = str(input("Введите строку даты: "))
print(convert_date(date_number))
