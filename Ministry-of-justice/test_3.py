# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def sum_current_time(time_str: str) -> int:
    """
    This function takes in a time string in the format HH:MM:SS
    The function returns the sum of all the numbers in the string
    For example, 01:02:03 should return 6.
    """
    list_of_nums = time_str.split(":")

    final_list = []
    for number in list_of_nums:
        number = int(number)
        final_list.append(number)

    return sum(final_list)


if __name__ == "__main__":

    print(sum_current_time('08:51:01'))
