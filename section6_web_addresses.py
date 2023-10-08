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


f = open(r"files\web.txt")
string = f.read()


def get_all_online_shopping():
    # * = 0 or 1 occurrence
    result = re.findall(r".+\s+(http.*://.+\.\w{2,})\s.+Online shopping.+", string)
    print(result)


def exercise_1():
    # Write a pattern on line 7, in between the double quotes, that will match the Site name (e.g. Google, Facebook
    #   etc.) of all the websites in the file that are based in China and have a 3-letter URL extension (e.g. .com,
    #   .org etc.).
    # regex by professor: r"(.+)\s+http.*://.+\.\w{3}\s.+China.+"
    result = re.findall(r"(.+)\s+http.+\.\w{3}\s.+China", string)
    print(result)


def exercise_2():
    # Write a pattern on line 7, in between the double quotes, that will match the URL and country of all the Social
    #   networking websites in the file whose domain name (excluding the extension) is less than 5 characters long.
    # regex by professor: r".+\s+(http.*://.{1,4}\.\w{2,})\s.+Social networking\s(.+?)\s.+"
    result = re.findall(r".+\s+(http.+//.{1,4}\.\w+)\s.+Social networking\s(.+?)\s.+", string)
    print(result)


def exercise_3():
    # Write a pattern on line 7, in between the double quotes, that will match the Site name (e.g. Google, Facebook
    #   etc.) and the web protocol of all the websites whose URLs contain subdomains (e.g. http://something.website.abc)
    # regex by professor: r"(.+)\s+(http.*)://.+\..+\.\w{2,}\s.+"
    result = re.findall(r"(.+)\s+(http.*)://.+\..+\.\w{2,}\s.+", string)
    print(result)


if __name__ == '__main__':
    # get_all_online_shopping()
    # exercise_1()
    # exercise_2()
    exercise_3()
