import pytest
from src.assignment import variables


def test_add_positive_numbers():
    assert variables.add(2, 3) == 5


def test_add_negative_numbers():
    assert variables.add(-1, -1) == -2


def test_is_variable_name_valid_true():
    assert variables.is_variable_name_valid('my_var')


def test_is_variable_name_valid_false():
    assert not variables.is_variable_name_valid('123bad')


def test_is_variable_name_type():
    assert not variables.is_variable_name_valid(123)
