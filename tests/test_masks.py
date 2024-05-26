#mport pytest

#rom src.masks import get_mask_cards, get_mask_bank_account


#pytest.mark.parametrize(
#numbers', 'number_list', [
#   ("7000792289606361", "7000 79** **** 6361"),
#   ("7158300734726758", "7158 30** **** 6758"),
#   ("6831982476737658", "6831 98** **** 7658"),
#   ("8990922113665229", "8990 92** **** 5229"),
#   ("5999414228426353", "5999 41** **** 6353")])
#
#ef test_get_mask_cards(numbers, number_list):
#  assert get_mask_cards(numbers) == number_list

import pytest
from src.masks import get_mask_cards, get_mask_bank_account

def test_get_mask_cards():
    assert get_mask_cards('7000792289606361') == '7000 79** **** 6361'


def test_get_mask_bank_account():
    assert get_mask_bank_account('73654108430135874305') == '**4305'

if __name__ == '__main__':
    pytest.main()
