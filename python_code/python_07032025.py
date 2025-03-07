'''
Problem: Log File Analysis

You are given a log file named server_logs.txt. Each line in the file represents a log entry with the following format:

[TIMESTAMP] [LEVEL] [MESSAGE]
TIMESTAMP: A timestamp in the format YYYY-MM-DD HH:MM:SS.
LEVEL: The log level, which can be INFO, WARNING, or ERROR.
MESSAGE: A text message describing the event.
Your task is to write a Python script that:

Reads the server_logs.txt file.
Counts the number of log entries for each log level (INFO, WARNING, ERROR).
Finds and prints the timestamp of the first ERROR log entry.
Finds and prints all the messages that contain the word "database".
Prints out a summary of the log file, including the counts of each log level, and the first error timestamp.

Example server_logs.txt:

[2023-10-26 10:00:00] INFO [Server started successfully.]
[2023-10-26 10:05:00] WARNING [Low disk space.]
[2023-10-26 10:10:00] ERROR [Database connection failed.]
[2023-10-26 10:15:00] INFO [User logged in.]
[2023-10-26 10:20:00] ERROR [File not found.]
[2023-10-26 10:25:00] WARNING [High CPU usage.]
[2023-10-26 10:30:00] INFO [Database query successful.]

Expected Output:

Log Level Counts:
INFO: 3
WARNING: 2
ERROR: 2

First ERROR Timestamp: 2023-10-26 10:10:00

Messages containing "database":
Database connection failed.
Database query successful.

Log File Summary:
Info log count: 3
Warning log count: 2
Error log count: 2
First error timestamp: 2023-10-26 10:10:00

'''
log_level_count = {'INFO': 0, 'WARNING':0, 'ERROR':0, 'First_error_timestamp':'', 'Database_message':[]}  
with open("files/server_logs.txt", 'r', encoding='utf-8') as logfile:
        for log in logfile:
            if 'INFO' in log:
                log_level_count['INFO'] += 1
            if 'WARNING' in log:
                log_level_count['WARNING'] += 1
            if 'Database' in log:
                index = log.find('Database')
                database_message = log[index:-2]
                log_level_count['Database_message'].append(database_message)
            if 'ERROR' in log:
                if log_level_count['ERROR'] == 0:
                    first_time_stamp = log[1:20]
                    log_level_count['First_error_timestamp'] = first_time_stamp
                log_level_count['ERROR'] += 1

info = log_level_count['INFO']
warning = log_level_count['WARNING']
error = log_level_count['ERROR']
timestamp = log_level_count['First_error_timestamp']
Log_Level_Counts = f'\nLog Level Counts:\nINFO:{info}\nWARNING:{warning}\nERROR:{error}\n'
print(Log_Level_Counts)
First_error_Timestamp = f'First ERROR Timestamp:{timestamp}'
print(First_error_Timestamp)
print('\nMessages containing "database":')
for message in log_level_count["Database_message"]:
 print(message)
Log_summary = f'\nLog File Summary:\nInfo log count:{info}\nWarning log count:{warning}\nError log count: {error}\nFirst error timestamp:{timestamp}'
print(Log_summary)


'''

Gemini modal answer below:

import re

def analyze_logs(log_file_path):
    """Analyzes a log file and prints summary information."""

    log_level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    first_error_timestamp = None
    database_messages = []

    try:
        with open(log_file_path, "r") as logfile:
            for line in logfile:
                match = re.match(r"\[(.*?)\]\s+(\w+)\s+\[(.*?)\]", line)
                if match:
                    timestamp, level, message = match.groups()
                    if level in log_level_counts:
                        log_level_counts[level] += 1
                    if level == "ERROR" and first_error_timestamp is None:
                        first_error_timestamp = timestamp
                    if "database" in message.lower():
                        database_messages.append(message)

        print("Log Level Counts:")
        for level, count in log_level_counts.items():
            print(f"{level}: {count}")

        if first_error_timestamp:
            print(f"\nFirst ERROR Timestamp: {first_error_timestamp}")
        else:
            print("\nNo ERROR logs found.")

        print('\nMessages containing "database":')
        for message in database_messages:
            print(message)

        print("\nLog File Summary:")
        print(f"Info log count: {log_level_counts['INFO']}")
        print(f"Warning log count: {log_level_counts['WARNING']}")
        print(f"Error log count: {log_level_counts['ERROR']}")
        print(f"First error timestamp: {first_error_timestamp}")

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
analyze_logs("files/server_logs.txt")

'''