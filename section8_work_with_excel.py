import openpyxl
import re


workbook = openpyxl.load_workbook(r"files\Employees.xlsx")

sheet = workbook["EmployeeData"]
data = []
for row in sheet.values:
    a, b, c, d, e, f, g = row
    data.append("{};{};{};{};{};{};{}".format(a, b, c, d, e, f, g))
employees = "\n".join(data)


def main():
    print(workbook.sheetnames)

    print(sheet.dimensions)
    for row in sheet.values:
        print(row)

    print(data)
    print("\n".join(data))

    print(employees)


def scenario_1():
    # get all last name from employees that salary start with 2, follow by number between 4 and 9 and follow by
    #   3 numbers
    result = re.findall(r"\d{1,};.+?;(.+?);.+;2[4-9]\d{3}", employees)
    print(result)


def scenario_2():
    # get all last name until 5 letters from employees that work in IT or Marketing departament

    # show with departament
    result = re.findall(r"\d{1,};.+?;(.{1,5});(IT|Marketing);.+;\d{5}", employees)
    print(result)

    # show without departament
    result = re.findall(r"\d{1,};.+?;(.{1,5});(?:IT|Marketing);.+;\d{5}", employees)
    print(result)


def scenario_3():
    # get all first name with start the letter between P and Z from employees that the phone start with 2 or 4 or 6
    #   or 8 and end with 1 or 3 or 5 or 7 or 9

    result = re.findall(r"\d+;([P-Z][a-z]+?);.+;[2468]\d{8}[13579];.+", employees)
    print(result)


def scenario_4():
    # get all first name, last name and phone from employees that works on Sales departament and location is New York
    result = re.findall(r"\d+;(.+?);(.+?);Sales;(.+?);.+New York;.+", employees)
    print(result)

    show_with_spaces = [" ".join(i) for i in result]
    print(show_with_spaces)


def scenario_5():
    # use negative lookahead assertion
    # get all last name from employees that location not finish with Miami
    result = re.findall(r"\d+;.+?;(.+?);.+?;.+?;.+, (?!Miami)", employees)
    print(result)
    print(len(result))


def exercise_1():
    # Having the data in our Excel file loaded into the employees variable (the same data we used throughout this
    #   section), use a regular expressions pattern with the findall() method to return the last names of all the
    #   employees working in two-letter word departments (IT or HR) and who earn more than 30000 dollars and less than
    #   60000.
    # professor solution: \d{1,};.+?;(.+?);\w{2};.+;[3-5]\d{4}
    result = re.findall(r"\d+;.+?;(.+?);(?:IT|HR);.+;[3-5]\d{4}", employees)
    print(result)


def exercise_2():
    # Having the data in our Excel file loaded into the employees variable (the same data we used throughout this
    #   section), use a regular expressions pattern with the findall() method to return the first and last names (as a
    #   list of tuples) of all the employees whose phone number ends with two consecutive odd digits (1,3,5,7 or 9).
    # professor solution: \d{1,};(.+?);(.+?);.+?;\d{8}[13579]{2};.+?;\d{5}
    result = re.findall(r"\d+;(.+?);(.+?);.+;\d{8}[13579]{2};.+", employees)
    print(result)


def exercise_3():
    # Having the data in our Excel file loaded into the employees variable (the same data we used throughout this
    #   section), use a regular expressions pattern with the findall() method to return the first name of each employee
    #   working in the IT department and whose last name starts with D.
    # professor solution: \d{1,};(.+?);D.+?;IT;.+;\d{5}
    result = re.findall(r"\d+;(.+?);D.+?;IT;.+", employees)
    print(result)


def exercise_4():
    # Having the data in our Excel file loaded into the employees variable (the same data we used throughout this
    #   section), use a regular expressions pattern with the findall() method to return the salaries of all the
    #   employees residing in Chicago or LA, and who work in the Logistics department.
    # professor solution: \d{1,};.+?;.+?;Logistics;\d{10};.+(?:Chicago|LA);(\d{5})
    result = re.findall(r".+;Logistics;.+;.+, (?:Chicago|LA);(\d{5})", employees)
    print(result)


def exercise_5():
    # Having the data in our Excel file loaded into the employees variable (the same data we used throughout this
    #   section), use a regular expressions pattern with the findall() method to return the last name and phone number
    #   of all employees who are located outside Las Vegas.
    # professor solution: \d{1,};.+?;(.+?);.+?;(.+?);.+, (?!Las Vegas)
    result = re.findall(r"\d+;.+?;(.+?);.+?;(\d+);.+, (?!Las Vegas)", employees)
    print(result)


if __name__ == '__main__':
    # main()
    # scenario_1()
    # scenario_2()
    # scenario_3()
    # scenario_4()
    # scenario_5()
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    exercise_5()
