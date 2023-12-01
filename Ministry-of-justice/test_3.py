"""This is a script that sums up the numbers in a timestamp"""

from datetime import datetime


def check_is_valid_timestamp(timestamp: str) -> bool:
    """Checks is a timestamp string is a valid timestamp value"""

    if not isinstance(timestamp, str):
        raise TypeError("Timestamp must be a string")
    try:
        datetime.strptime(timestamp, "%H:%M:%S")
        return True
    except ValueError:
        return False


def sum_current_time(time_str: str) -> int:
    """
    This function takes in a time string in the format HH:MM:SS
    The function returns the sum of all the numbers in the string
    For example, 01:02:03 should return 6.
    """

    if not isinstance(time_str, str):
        raise TypeError('The time_str input must be a string')

    if not check_is_valid_timestamp(time_str):
        raise ValueError("The input is not a valid time")

    list_of_nums = time_str.split(":")

    final_list = []
    for number in list_of_nums:
        number = int(number)
        final_list.append(number)

    return sum(final_list)


if __name__ == "__main__":

    print(sum_current_time('08:51:01'))
