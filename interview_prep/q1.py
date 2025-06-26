'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
'''

#my solution
# def make_readable(seconds):
#     if seconds < 60:
#         if len(str(seconds)) < 2:
#             seconds = f"0{seconds}"
#         return f"00:00:{seconds}"
#     elif seconds < 3600:
#         if seconds == 60:
#             return "00:01:00"
#         else:
#             seconds_for_minutes = seconds - 59
#             minutes = int(seconds_for_minutes/60)
#             return f"00:{minutes}:59"
#     if seconds >= 3600:
#         if seconds == 3600:
#             return "01:00:00"
#         elif seconds%3600 == 0:
#             hours = int(seconds/3600)
#             return f"{hours}:00:00"
#         else:
#             seconds_for_minutes = seconds - 59
#             minutes = seconds_for_minutes/60
#             if minutes > 59:
#                 minutes_for_hours = minutes - 59
#                 hours = int(minutes_for_hours/60)
#                 return f"{hours}:59:59"


# modal solution
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"