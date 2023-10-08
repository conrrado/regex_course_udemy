import re


string = "The Euro STOXX 600 index, STOXX which tracks " + \
             "all stock markets across Europe including the " + \
             "FTSE, fell by 11.48% – the worst day since it " + \
             "launched in 1998. The panic selling prompted by " + \
             "the coronavirus has wiped £2.7tn off the value of " + \
             "STOXX 600 shares since its all-time peak on 19 " + \
             "February."
string_with_new_line = "The Euro STOXX 600 index, which tracks " + \
             "all stock markets across Europe including the " + \
             "FTSE, fell by 11.48% – the worst day since it " + \
             "launched in 1998.\nThe panic selling prompted by " + \
             "the coronavirus has wiped £2.7tn off the value of " + \
             "STOXX 600 shares since its all-time peak on 19 " + \
             "February."


def extension_notation():
    # general syntax: (?...)
    # The dot (.) matches any character except the newline \n, by default
    # + = that means precede character can be repeat one or more time
    result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
    print(result)  # show all text because only .+ matches any character one or more time
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    # ?: = non-capturing group
    result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))


def extension_named_groups():
    # general syntax: (?P<name>...)
    result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    # group 1 name: wordex
    # group 2 name: uppercase
    # group 3 name: date
    result = re.search(r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string)
    print(result.groups())
    print(result.group("wordex"))
    print(result.group("uppercase"))
    print(result.group("date"))
    print(result.groupdict())


def extension_positive_lookahead_assertions():
    # general syntax: (?=...)
    # match all and need be following by something
    result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
    print(result)
    result = re.findall(r"Euro(?=[a-z]+)", string)
    print(result)


def extension_negative_lookahead_assertions():
    # general syntax: (?!...)
    # \d(?![5-9]|\D) = match all one digit and can't be following by [5-9] or non-digit
    # for example, considering the text: '600 ', the first number is following by 0, the second is following by 0 too,
    #       but the third is following by space, so that digit not satisfy the condition
    result = re.findall(r"\d(?![5-9]|\D)", string)
    print(result)
    # \b\w+\b(?!\s) = need to be a word with 1 or more characters and can't be following by space, \n, \t, \r, \f or \v
    result = re.findall(r"\b\w+\b(?!\s)", string)
    print(result)


def extension_positive_lookbehind_assertions():
    # general syntax: (?<=...)
    # (?<=\s)\d{1,} = match all number that preceding with \s (space, \n, \t, \r, \f or \v)
    result = re.findall(r"(?<=\s)\d{1,}", string)
    print(result)
    # (?<=,\s)\b\w+\b = match all words that preceding with ',' and then \s
    result = re.findall(r"(?<=,\s)\b\w+\b", string)
    print(result)


def extension_negative_lookbehind_assertions():
    # general syntax: (?<!...)
    # (?<!\s)\d{1,} = match all number that can't be preceding with \s
    result = re.findall(r"(?<!\s)\d{1,}", string)
    print(result)
    # re.I = ignore case
    # (?<!x)x(?!x) = match a letter x and can't be preceding by x and can't be following by x
    result = re.findall(r"(?<!x)x(?!x)", string, re.I)
    print(result)


if __name__ == '__main__':
    # extension_notation()
    # extension_named_groups()
    # extension_positive_lookahead_assertions()
    # extension_negative_lookahead_assertions()
    extension_positive_lookbehind_assertions()
    # extension_negative_lookbehind_assertions()
