"""Testing the functions in test_3.py"""

import pytest

from test_3 import sum_current_time, check_is_valid_timestamp


def test_sum_current_time_valid_input():
    """Test that checks the function is working"""

    time_str = '08:51:01'

    assert sum_current_time(time_str) == 60


def test_sum_current_time_working_invalid_input_type():
    """Test that checks the function will raise an error
        when the input is not a string"""

    time_str = 22

    with pytest.raises(TypeError):
        sum_current_time(time_str)


def test_sum_current_time_not_a_valid_timestamp():
    """Test that checks the function raises an error
    when the input is not a valid timestamp"""

    time_str = '08:30:05:11'

    with pytest.raises(ValueError):
        sum_current_time(time_str)


def test_sum_current_time_not_a_timestamp_negative_value():
    """Test that checks the function raises an error
    when the input is an invalid timestamp"""

    time_str = '08:-1:05'

    with pytest.raises(ValueError):
        sum_current_time(time_str)


def test_check_is_valid_timestamp_True():
    """Test that checks the function returns True for a valid timestamp"""

    timestamp = "08:51:01"

    assert check_is_valid_timestamp(timestamp) == True


def test_check_is_valid_timestamp_False():
    """Test that checks the function returns False for a invalid timestamp"""

    timestamp = "08:-1:01"

    assert check_is_valid_timestamp(timestamp) == False
