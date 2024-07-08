from collections import defaultdict


def count_operations_by_category(bank_operations_list, categories):
    """
    Функция для подсчета количества операций в каждой категории.
    """
    category_count = defaultdict(int)

    for operation in bank_operations_list:
        description = operation.get('description', '').lower()
        if description in categories:
            category_count[description] += 1

    return dict(category_count)


# Пример использования
if __name__ == "__main__":
    bank_operations_list = [
        {'amount': 100, 'description': 'groceries'},
        {'amount': 200, 'description': 'entertainment'},
        {'amount': 150, 'description': 'groceries'},
        {'amount': 50, 'description': 'utilities'},
    ]

    categories = ['groceries', 'entertainment', 'utilities']

    result = count_operations_by_category(bank_operations_list, categories)
    print(result)  # {'groceries': 2, 'entertainment': 1, 'utilities': 1}
