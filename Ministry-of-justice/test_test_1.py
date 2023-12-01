"""Testing the functions in test_1.py"""

from test_1 import is_log_line, check_is_valid_timestamp, get_dict


def test_is_log_line_working_True():
    line = "03/11/21 08:51:01 INFO    :.main: *************** RSVP Agent started ***************"

    assert is_log_line(line) == True


def test_is_log_line_working_False():
    line = "01"

    assert is_log_line(line) == False


def test_check_is_valid_timestamp_True():
    timestamp = "03/11/21 08:51:01"

    assert check_is_valid_timestamp(timestamp) == True


def test_check_is_valid_timestamp_False():
    timestamp = "03/13/21 08:51:01"

    assert check_is_valid_timestamp(timestamp) == False


def test_get_dict_working():
    line = "03/11/21 08:51:01 INFO    :.main: *************** RSVP Agent started ***************"

    assert get_dict(line) == {"timestamp": "03/11/21 08:51:01",
                              "log_level": "INFO",
                              "message": ":.main: *************** RSVP Agent started ***************"}


def test_get_dict_working_invalid_input():
    line = "01"

    assert get_dict(line) == None
