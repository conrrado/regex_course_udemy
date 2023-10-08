import pandas


def main():
    d = pandas.DataFrame()
    print(type(d))

    d = pandas.DataFrame([
        ['Andy', 46, 'Engineer'],
        ['Jane', 33, 'Nurse'],
        ['Robert', 21, 'Student'],
        ['Maria', 30, 'Student']
    ])
    print(f"\n{d}")

    d = pandas.DataFrame([
        ['Andy', 46, 'Engineer'],
        ['Jane', 33, 'Nurse'],
        ['Robert', 21, 'Student'],
        ['Maria', 30, 'Student']
    ],
        columns=["Name", "Age", "Occupation"])
    print(f"\n{d}")

    d = pandas.DataFrame([
        ['Andy', 46, 'Engineer'],
        ['Jane', 33, 'Nurse'],
        ['Robert', 21, 'Student'],
        ['Maria', 30, 'Student']
    ],
        columns=["Name", "Age", "Occupation"],
        index=["ID1", "ID2", "ID3", "ID4"])
    print(f"\n{d}")

    print(f"\n{d.Name}")

    print(f"\n{d.Age}")


def get_html():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    d = pandas.read_html(url)
    print(d)

    d = pandas.read_html(url)[1]
    print(f"\n{d}")


if __name__ == '__main__':
    # main()
    get_html()
