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


f = open(r"files\stocks.txt")
string = f.read()


def get_all_companies_that_revenue_less_than_50b():
    # + = occurring 1 or more time
    result = re.findall(r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-4][0-9]\.[0-9]+B\s+[0-9]+\.[0-9]+", string)
    print(result)


def exercise_1():
    # Write a pattern on line 7, in between the double quotes, that will match the company names whose revenue is
    #   between 10B and 30B and P/E ratio is between 10 and 15.
    # result = re.findall(r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-2][0-9]\.[0-9]+B\s+1[0-4]\.[0-9]+", string)
    result = re.findall(r"(.+?)\s+[0-9]+.+\s+(?:[1-2][0-9]\.[0-9]+B|30\.[0-9]+B)\s+(?:1[0-4]\.[0-9]+|15.[0-9]+)", string)
    print(result)


def exercise_2():
    # Write a pattern on line 7, in between the double quotes, that will match the company names whose average volume is
    #   less than 10M.
    # result = re.findall(r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-2][0-9]\.[0-9]+B\s+1[0-4]\.[0-9]+", string)
    result = re.findall(r"(.+?)\s+[0-9]\.[0-9]+M\s+", string)
    print(result)


def exercise_3():
    # Write a pattern on line 7, in between the double quotes, that will match the companies names whose Average Volume
    #   starts with an even digit (2, 4, 6 or 8), and their P/E ratio ends with an odd digit (1, 3, 5, 7 or 9).
    # result = re.findall(r"(.+?)\s+[2468][0-9]*\.[0-9]+M\s+[0-9]+\.[0-9]+B\s+[0-9]+\.[0-9][13579]", string)
    result = re.findall(r"(.+?)\s+[2468][0-9]*\.[0-9]+M\s+[0-9]+\.[0-9]+B\s+[0-9]+\.[0-9]*[13579]\s", string)
    print(result)


if __name__ == '__main__':
    # get_all_companies_that_revenue_less_than_50b()
    # exercise_1()
    # exercise_2()
    exercise_3()
