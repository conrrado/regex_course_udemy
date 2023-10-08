import re


string = "The Euro STOXX 600 index, which tracks " + \
             "all stock markets across Europe including the " + \
             "FTSE, fell by 11.48% – the worst day since it " + \
             "launched in 1998. The panic selling prompted by " + \
             "the coronavirus has wiped £2.7tn off the value of " + \
             "STOXX 600 shares since its all-time peak on 19 " + \
             "February."

def raw_strings():
    # The 're' module
    #help(re)
    #print(dir(re))

    # Raw strings
    path = r"C:\Users\tasks\new"
    # se não usar o r, o python vai interpretar os comandos \t, \n...
    path = "C:\tasks\new"
    print(path)


def re_compile():
    # \d = digitos

    s = r"\d{4}"
    print(type(s))

    t = re.compile(s)
    print(type(t))

    result = re.findall(t, string)
    print(result)


def re_search():
    result = re.search(r"\d{3}", string)
    print(result)
    # re.Match é o tipo do objeto, span é a posição da primeira ocorrência, 600 é o valor
    # <re.Match object; span=(15, 18), match='600'>
    print(type(result))
    print(string[15:18])


def re_match():
    # \w = A word character is a character a-z, A-Z, 0-9, including _ (underscore), but doesn't match white spaces

    result = re.match(r"\w{3}", string)
    print(result)

    result = re.match(r"\w{4}", string)
    print(result)


def re_fullmatch():
    # . = matches any character except the new line character (\n)

    print(len(string))
    result = re.fullmatch(r".{285}", string)
    print(result)


def re_findall():
    result = re.findall(r"\d{3}", string)
    print(result)  # ['600', '199', '600']
    result = re.findall(r"\d{5}", string)
    print(result)  # []


def re_split():
    result = re.split(r"\s", string)
    print(result)


def re_sub():
    # [A-Z]: caracteres de A a Z maiuculo, {2,}: que esses caracteres repitam pelo menos 2X
    result = re.sub(r"[A-Z]{2,}", "INDEX", string)
    print(result)
    # replace somente 2 vezes
    result = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
    print(result)


def re_subn():
    # exibe entre '' e a quantidade que achou
    result = re.subn(r"[A-Z]{2,}", "INDEX", string)
    print(result)


def re_group():
    # .+ = qualquer caracter ou espaço na mesma linha
    # cada grupo de parenteses é uma pesquisa a ser feita
    # .+ex = qualquer coisa que termine com ex
    # \d = digito
    # \s = espaço
    result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
    # print(result)
    # print(result.group())
    print(result.groups())
    print(result.group(1))
    print(result.group(2))


def re_start_end_span():
    result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
    print(result.groups())
    print(result.group(1))
    print(result.start(1))
    print(string.index("index"))
    print('\n')
    print(result.groups())
    print(result.group(2))
    print(result.start(2))
    print(string.index("19 February"))
    print('\n')
    print(result.end(1))
    print(result.end(2))
    print('\n')
    print(string[19:24])
    print(string[273:284])
    print('\n')
    print(result.span(1))
    print(result.span(2))


def optional_flags():
    # re.I - ignorecase
    # re.S - dotall
    # re.X - verbose
    result = re.findall(r"the", string)
    print(result)
    # using flag ignorecase
    result = re.findall(r"the", string, re.I)
    print(result)
    # using flag dotall
    string2 = "Hello\nPython"
    result = re.search(r".+", string2)
    print(result)
    result = re.search(r".+", string2, re.S)
    print(result)
    # using flat verbose
    result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
    print(result.groups())
    result = re.search(r""".+\s #Beginning of the string
                        (.+ex) #Searching for index
                        .+ #Middle of the string
                        (\d\d\s.+). #Date at the end""", string, re.X)
    print(result.groups())


if __name__ == '__main__':
    # raw_strings()
    # re_compile()
    # re_search()
    # re_match()
    # re_fullmatch()
    # re_findall()
    # re_split()
    # re_sub()
    # re_subn()
    re_group()
    # re_start_end_span()
    # optional_flags()

# exceptions:
# Whenever you get the AttributeError: 'NoneType' object has no attribute 'group’ or ‘groups’ exception, it means that
# your pattern syntax is incorrect, a match was not found and the value being returned is None, thus you must rethink
# your pattern or spot your mistakes.
