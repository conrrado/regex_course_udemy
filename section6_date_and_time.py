import re


# https://stackoverflow.com/questions/14213848/difference-between-and
# Both will match any sequence of one or more characters. The difference is that:
#
# .+ is greedy and consumes as many characters as it can.
# .+? is reluctant and consumes as few characters as it can.
#
# Thus:
#
# e.+d finds the longest substring that starts with e and ends with d (and contains at least one character in between).
#   In your example extend cup end will be found.
# e.+?d find the shortest such substring. In your example, extend and end are two such non-overlapping matches, so it
#   finds both.


f = open(r"files\logs.txt")
string = f.read()


def get_all_critical_logs():
    result = re.findall(r"Critical 1/1[1-6]/2020 .+ [A-Z]{2} (.+?) \d+", string)
    print(result)


def exercise_1():
    # Write a pattern on line 7, in between the double quotes, that will match the Source substring of all the log
    #   entries that were generated after 12 PM and before 4 PM, regardless of the severity level and the date.
    # regex by professor: r".+/2020 (?:12|[1-3]):\d\d:\d\d PM (.+?) \d+"
    result = re.findall(r".+/2020 (?:12|[1-3]):\d\d:\d\d PM (.+?) \d+", string)
    print(result)


def exercise_2():
    # Write a pattern on line 7, in between the double quotes, that will match the Date of all the log entries that
    #   have TPM as the Source of the log message.
    # regex by professor: r".+ (.+?) \d+:\d+:\d+ [A-Z]{2} TPM \d+"
    result = re.findall(r".+ (.+) .+ \w{2} TPM \d+", string)
    print(result)


def exercise_3():
    # Write a pattern on line 7, in between the double quotes, that will match the Date and Time of all the log entries
    #   that have been generated between 24 and 27 of January 2020 and between 8:00:00 and 8:59:59 AM.
    # regex by professor: r".+ (1/2[4-7]/2020 8:\d+:\d+) "
    result = re.findall(r".+ (1/2[4-7]/2020 8:[0-5]\d:[0-5]\d) AM .+", string)
    print(result)


if __name__ == '__main__':
    # get_all_critical_logs()
    exercise_1()
    # exercise_2()
    # exercise_3()
