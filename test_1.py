"""Script that validates log lines and converts each line into a dictionary"""

from datetime import datetime

VALID_LOG_LEVEL = ['INFO', 'WARNING', 'TRACE']


def check_is_valid_timestamp(timestamp: str) -> bool:
    """Checks is a timestamp string is a valid timestamp value"""

    if not isinstance(timestamp, str):
        raise TypeError("Timestamp must be a string")
    try:
        datetime.strptime(timestamp, "%d/%m/%y %H:%M:%S")
        return True
    except ValueError:
        return False


def is_log_line(line: str) -> bool:
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    if not isinstance(line, str):
        raise TypeError("Line must be a string")

    parts = line.split()

    if len(parts) >= 4:
        timestamp = f"{parts[0]} {parts[1]}"
        error_type = parts[2]
        message = " ".join(parts[3:])
        if check_is_valid_timestamp(timestamp) and error_type and message:
            return True
    return False


def get_dict(line) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    if not isinstance(line, str):
        raise TypeError("Line must be a string")

    parts = line.split()

    if len(parts) >= 4:
        timestamp = f"{parts[0]} {parts[1]}"
        log_level = parts[2]
        message = " ".join(parts[3:])

        if check_is_valid_timestamp(timestamp) and message:
            if log_level in VALID_LOG_LEVEL:
                return {"timestamp": timestamp, "log_level": log_level, "message": message}



# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
