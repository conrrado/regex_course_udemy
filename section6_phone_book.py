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


f = open(r"files\phone.txt")
string = f.read()


def get_all_last_name_and_phone_without_core_area_by_core_area_finished_with_0():
    # regex by professor: r".+ (.+)\t\(\d\d0\)\s(.+)"
    result = re.findall(r".+ (\w+?)\t\(\d\d0\)\s(\d{3}-\d+)", string)
    print(result)


def get_all_code_area_by_number_finished_by_7():
    # regex by professor: r".+\t\((\d{3})\)\s.{7}7"
    result = re.findall(r".+\t\((\d{3})\)\s.{7}7", string)
    print(result)


def exercise_1():
    # Write a pattern on line 7, in between the double quotes, that will match all the persons (first and last name) in
    #   the file whose phone number starts with an odd digit (1, 3, 5, 7, 9).
    # regex by professor: r"(.+)\t\(\d{3}\) [13579].{7}"
    result = re.findall(r"(.+)\t.+\s[13579].{7}", string)
    print(result)


def exercise_2():
    # Write a pattern on line 7, in between the double quotes, that will match all the persons (first name only) in the
    #   file whose area code is a number less than 300.
    # regex by professor: r"(.+) .+\t\([0-2]\d\d\) .{8}"
    result = re.findall(r"(.+?) .+\t\([0-2][0-9]{2}\)", string)
    print(result)


def exercise_3():
    # Write a pattern on line 7, in between the double quotes, that will match all the persons (first name only) in the
    #   file whose last name ends in a vowel (aeiou) and phone number ends in either 0, 7 or 9
    # r"(.+) .+[aeiou]\t\(\d{3}\) .{7}[079]"
    result = re.findall(r"(.+?) .+[aeiou]\t.+-\d{3}[079]", string)
    print(result)


if __name__ == '__main__':
    # get_all_last_name_and_phone_without_core_area_by_core_area_finished_with_0()
    # get_all_code_area_by_number_finished_by_7()
    # exercise_1()
    # exercise_2()
    exercise_3()
