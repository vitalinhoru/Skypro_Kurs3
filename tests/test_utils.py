import os

import pytest
from src.utils import *


@pytest.fixture
def testing_func():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.split(current_dir)[0]
    base = os.path.join(root_dir, 'data', 'test.json')
    with open(base, 'r', encoding='UTF=8') as file:
        data = json.load(file)
    return data


def test_get_correct_date(testing_func):
    assert get_correct_date(testing_func[0]['date']) == '29.11.2018'
    assert get_correct_date(testing_func[1]['date']) == '12.09.2018'
    assert get_correct_date(testing_func[2]['date']) == '19.08.2018'


def test_get_right_transactions(testing_func):
    assert len(get_right_transactions(testing_func)) == 2


def test_get_last_five_transactions(testing_func):
    assert len(get_last_five_transactions(testing_func)) == 3


def test_hide_from(testing_func):
    assert hide_from(testing_func[0]) == 'MasterCard 3152 47** **** 5065'
    assert hide_from(testing_func[1]) == 'Visa Platinum 1246 37** **** 3588'
    assert hide_from(testing_func[2]) == 'Visa Classic 6831 98** **** 7658'


def test_hide_to(testing_func):
    assert hide_to(testing_func[0]) == 'Visa Gold **5960'
    assert hide_to(testing_func[1]) == 'Счет **1657'
    assert hide_to(testing_func[2]) == 'Visa Platinum **5229'
