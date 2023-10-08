import re


string = "The Euro STOXX 600 index, which tracks " + \
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


def the_dot():
    # The dot (.) matches any character except the newline \n, by default
    # + = is greedy and consumes as many characters as it can.
    result = re.search(r"(.+)", string)
    print(result)
    print(result.group(1))


def the_caret():
    # The caret (^) matches only at the beginning of the line
    # \w - A word character is a character a-z, A-Z, 0-9, including _ (underscore), but doesn't match white spaces
    # re.M - multiline
    result = re.search(r"^\w{3}", string)
    print(result)
    result = re.findall(r"^\w{3}", string_with_new_line, re.M)
    print(result)


def the_dollar_sign():
    # The dollar sign ($) matches at the end of the line
    # \W matches any non-alphanumeric character (anything besides letters, digits and the underscore)
    # \W it is the opposite of \w
    # re.M - multiline
    result = re.findall(r"\s(\w{2,})\W$", string_with_new_line, re.M)
    print(result)


def the_asterisk():
    # The asterisk (*) matches 0 or more repetitions of the preceding expression, in a greedy way
    result = re.findall(r"\d\d\d*", string)
    print(result)
    # r"E.* " = Start with capital letter E, matches any characters except new line, 0 or more repetitions and finally
    #   with space
    result = re.findall(r"E.* ", string)
    print(result)
    # r"E\w*" = Start with capital letter E, matches a character a-z, A-Z, 0-9, including _ (underscore) but
    #   doesn't match white spaces, 0 or more repetitions
    result = re.findall(r"E\w*", string)
    print(result)


def the_plus_sign():
    # The plus sign (+) matches 1 or more repetitions of the preceding expression. By default, the matching is greedy.
    result = re.findall(r"\d\d\d+", string)
    print(result)
    # r"E.+ " = Start with capital letter E, matches any character except the newline \n, 1 or more repetition and
    #   finish with space
    result = re.findall(r"E.+ ", string)
    print(result)
    # r"E\w+" = Start with capital letter E, matches a character a-z, A-Z, 0-9, including _ (underscore) but doesn't
    #   match white spaces, 1 or more repetition
    result = re.findall(r"E\w+", string)
    print(result)


def the_question_mark():
    # The question mark (?) matches 0 or 1 repetition of the preceding expression.
    result = re.findall(r"\d\d\d?", string)
    print(result)
    # r"E.? " = Start with capital letter E, matches any character except the newline \n, 0 or 1 repetition and finish
    #   with space
    result = re.findall(r"E.? ", string)
    print(result)
    # r"E\w?" = Start with capital letter E, matches a character a-z, A-Z, 0-9, including _ (underscore) but doesn't
    #   match white spaces, 0 or 1 repetition
    result = re.findall(r"E\w?", string)
    print(result)


def greedy_vs_non_greedy():
    # The question mark (?) after the asterisk, plus sign or question mark turns off the greedy behavior completely
    # Syntax: *? or +? or ??
    # The asterisk (*) matches 0 or more repetitions of the preceding expression
    result = re.findall(r"\d\d\d*", string)
    print(result)
    # *? = 0 repetitions of the preceding expression
    result = re.findall(r"\d\d\d*?", string)
    print(result)
    # The plus sign (+) matches 1 or more repetitions of the preceding expression
    result = re.findall(r"\d\d\d+", string)
    print(result)
    # +? = is reluctant and consumes as few characters as it can.
    result = re.findall(r"\d\d\d+?", string)
    print(result)
    # The question mark (?) matches 0 or 1 repetition of the preceding expression.
    result = re.findall(r"\d\d\d?", string)
    print(result)
    # ?? = 0 repetitions of the preceding expression
    result = re.findall(r"\d\d\d??", string)
    print(result)


def the_backslash():
    # The backslash (\) can have any of these two roles:
    #   - Signals a special sequence (\d, \w etc)
    #   - Escaping and matching a symbol with special meaning in regex syntax (\. or \?)
    # find all that matches with 1 digit
    result = re.findall(r"\d", string)
    print(result)
    # find all that matches with "." symbol
    result = re.findall(r"\.", string)
    print(result)


def the_square_brackets():
    # Square brackets ([]) represent sets of characters and character classes
    # [wxkq] = find all that matches "w" or "x" or "k" or "q"
    result = re.findall(r"[wxkq]", string)
    print(result)
    # [a-d] = find all that matches "a" or "b" or "c" or "d"
    result = re.findall(r"[a-d]", string)
    print(result)
    # [S-W] = find all that matches from "S" to "W" in capital letters
    result = re.findall(r"[S-W]", string)
    print(result)
    # [1-5] = find all that matches from "1" to "5" digital
    result = re.findall(r"[1-5]", string)
    print(result)
    # Two consecutive letters, the first letter from a to f, the second letter from c to w
    result = re.findall(r"[a-f][c-w]", string)
    print(result)
    # Two consecutive digits, the first digit from 0 to 5, the second digit from 7 to 9
    result = re.findall(r"[0-5][7-9]", string)
    print(result)
    # One number then one letter
    result = re.findall(r"[0-9][a-z]", string)
    print(result)
    # [^...] = negation
    # [^X] = return all characteres except capital X
    result = re.findall(r"[^X]", string)
    print(result)
    print("X" in result)
    # inside brackets the special characteres 'loosers superpower'
    # [(.+?)] = return all mathes with '(' '.' '+' '?' ')'
    result = re.findall(r"[(.+?)]", string)
    print(result)


def character_classes():
    result = re.findall(r"[0-9]", string)
    print(result)
    result = re.findall(r"[a-zA-Z]", string)
    print(result)
    result = re.findall(r"[^0-9]", string)
    print(result)
    # Whitespace characters:
    # - Space (from the keyboard)
    # - New line character (\n)
    # - Tab character (\t)
    # - Carriage return (\r)
    # - Form feed (\f)
    # - Vertical tab (\v)
    result = re.findall(r"[ \n\t\r\f\v]", string)
    print(result)
    print(len(result))
    print(string.count(" "))
    result = re.findall(r"[^ \n\t\r\f\v]", string)
    print(result)
    result = re.findall(r"[a-zA-Z0-9_]", string)
    print(result)
    result = re.findall(r"[^a-zA-Z0-9_]", string)
    print(result)


def the_curly_braces():
    # The curly braces ( {} ) are a repetition operator in regular expression patterns.
    # \b = borders of the word
    # \b\w{4}\b = matches all words or sequence of numbers that have 4 characters
    result = re.findall(r"\b\w{4}\b", string)
    print(result)
    # \b\w{3,5}\b = matches all words or sequence of numbers that have 3, 4, or 5 characters
    result = re.findall(r"\b\w{3,5}\b", string)
    print(result)
    # \b\w{3,5}\b = matches all words or sequence of numbers that have at least 3 characters
    result = re.findall(r"\b\w{3,}\b", string)
    print(result)

    number = "123465789123465789"
    result = re.search(r"\d{3,6}", number)
    print(result)
    # \d{3,6}? is equivalent \d{3}
    result = re.search(r"\d{3,6}?", number)
    print(result)


def the_pipe():
    # The pip metacharacter ( | ) == OR
    result = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string)
    print(result)
    result = re.search(r"\d{8}|\d{4}|\b[A-Z]{4}\b", string)
    print(result)


def special_sequences_a_and_z():
    # \A and \Z
    # ^([A-Z].*?)\s = start with uppercase letter,
    #       The dot (.) matches any character except the newline \n,
    #       *? = 0 repetitions of the preceding expression
    #       ^ = beginning of the phrase
    result = re.findall(r"^([A-Z].*?)\s", string_with_new_line, re.M)
    print(result)
    # \A = match one time on the first of the phrase
    result = re.findall(r"\A([A-Z].*?)\s", string_with_new_line, re.M)
    print(result)
    # \W = matches of non-alphanumeric characters such as symbols, space or point
    # \Z = matches one time on the end of the phrase
    result = re.findall(r"\W\Z", string_with_new_line, re.M)
    print(result)
    # $ = matches on the end of the line
    result = re.findall(r"\W$", string_with_new_line, re.M)
    print(result)


def special_sequences_b():
    # \b = borders of the word
    # \b\w{10,}\b = matches a word with at least 10 characters
    # \w - A word character is a character a-z, A-Z, 0-9, including _ (underscore), but doesn't match white spaces
    result = re.findall(r"\b\w{10,}\b", string)
    print(result)
    # \B is opposite \b, so the matches with inside the word
    result = re.findall(r"\Bcross", string)
    print(result)


def special_sequences_d():
    # \d = matches any digits from 0 to 9 [0-9]
    # (\d)[a-z] = search by a match with digits and then a letter, but only show digits because is in a group ()
    result = re.findall(r"(\d)[a-z]", string)
    print(result)
    # \D is equivalent to [^0-9]
    result = re.findall(r"\W\D\W", string)
    print(result)
    result = re.findall(r"\W(\D)\W", string)
    print(result)


def special_sequence_s():
    # \s = ["space"\n\t\r\f\v]
    result = re.findall(r"\s", string_with_new_line)
    print(result)
    # \S = ^\s
    # \S{8,} = matches any character (exception \s) at least 8 characters
    result = re.findall(r"\S{8,}", string)
    print(result)


def special_sequence_w():
    # \w - A word character is a character a-z, A-Z, 0-9, including _ (underscore), but doesn't match white spaces
    result = re.findall(r"\s(\w{3,5})\s", string)
    print(result)
    # \W = ^\w
    result = re.findall(r"\W", string)
    print(result)


if __name__ == '__main__':
    # the_dot()
    # the_caret()
    # the_dollar_sign()
    # the_asterisk()
    # the_plus_sign()
    # the_question_mark()
    # greedy_vs_non_greedy()
    # the_backslash()
    the_square_brackets()
    # character_classes()
    # the_curly_braces()
    # the_pipe()
    # special_sequences_a_and_z()
    # special_sequences_b()
    # special_sequences_d()
    # special_sequence_s()
    # special_sequence_w()
