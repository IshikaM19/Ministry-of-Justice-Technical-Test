"""Testing the functions in test_3.py"""

import pytest

from test_3 import sum_current_time, check_is_valid_timestamp


def test_sum_current_time_valid_input():
    time_str = '08:51:01'

    assert sum_current_time(time_str) == 60


def test_sum_current_time_working_invalid_input_type():
    time_str = 22

    with pytest.raises(TypeError):
        sum_current_time(time_str)


def test_sum_current_time_invalid_input():
    time_str = '08:30:05:11'

    with pytest.raises(ValueError):
        sum_current_time(time_str)


def test_sum_current_time_not_a_timestamp():
    time_str = '08:-1:05'

    with pytest.raises(ValueError):
        sum_current_time(time_str)


def test_check_is_valid_timestamp_True():
    timestamp = "08:51:01"

    assert check_is_valid_timestamp(timestamp) == True


def test_check_is_valid_timestamp_False():
    timestamp = "08:-1:01"

    assert check_is_valid_timestamp(timestamp) == False
