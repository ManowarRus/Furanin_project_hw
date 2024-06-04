import pytest

from src.decorators import log

# Тест записи в файл при успешной работе функции.
def test_log_file():
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)
    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok. Result: 500\n"
    assert result == 500


# Тест вывода в консоль при успешной работе функции.
def test_log_console(capsys):
    @log()
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500
