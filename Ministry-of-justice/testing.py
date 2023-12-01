
file = '03/11/21 08:51:01 INFO    :.main: *************** RSVP Agent started ***************'

parts = file.split()
timestamp = f"{parts[0]} {parts[1]}"
error_type = parts[2]
message = ' '.join(parts[3:])

print(timestamp, error_type, message)
