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


f = open(r"files\bookshelf.txt")
string = f.read()


def get_all_title():
    # The dot (.) matches any character except the newline \n, by default
    # +? = is reluctant and consumes as few characters as it can.
    result = re.findall(r".+?;(.{1,25});.+?", string)
    print(result)  # get all book title


def get_all_author_from_2000():
    # The dot (.) matches any character except the newline \n, by default
    # +? = is reluctant and consumes as few characters as it can.
    result = re.findall(r"(.+?);.+?;20[0-9][0-9]", string)
    print(result)


def exercise_1():
    # Write a pattern on line 7, in between the double quotes, that will match all the book titles in the file that
    #   end with the letter p.
    result = re.findall(r".+?;(.+p);.+?", string)
    print(result)


def exercise_2():
    # Write a pattern on line 7, in between the double quotes, that will match all the authors in the file whose last
    #   name starts with the letter B.
    result = re.findall(r".+? (B.+?);.+?;.+?", string)
    print(result)


def exercise_3():
    # Write a pattern on line 7, in between the double quotes, that will match all the books in the file that have been
    #   published between 1980 and 1999.
    result = re.findall(r".+?;(.+?);19[8-9][0-9]", string)
    print(result)


if __name__ == '__main__':
    # get_all_title()
    # get_all_author_from_2000()
    # exercise_1()
    # exercise_2()
    exercise_3()
