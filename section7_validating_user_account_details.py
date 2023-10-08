import re


def validating_userinfo():
    # Asking the user for the first name and checking the format
    # Does not contain any other characters besides letters.
    #
    # It starts with a capital letter and all the other letters are lowercase.
    #
    # Is at least 2 characters long.
    while True:
        fname = input("\nPlease enter your First Name: ")

        check = re.fullmatch(r"[A-Z][a-z]+", fname)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the last name and checking the format
    # Does not contain any other characters besides letters.
    #
    # It starts with a capital letter and all the other letters are lowercase.
    #
    # Is at least 2 characters long.
    while True:
        lname = input("\nPlease enter your Last Name: ")

        check = re.fullmatch(r"[A-Z][a-z]+", lname)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the date of birth and checking the format
    # The person was born before January 1st 2002.
    #
    # Contains only digits and forward slashes.
    #
    # Follows the format MM/DD/YYYY
    while True:
        date = input("\nPlease enter your Date of Birth (mm/dd/yyyy): ")

        # other way: (0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(200[2-9]|20[1-9][0-9])
        check = re.fullmatch(r"(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/(200[2-9]|20[1-9][0-9])", date)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the email address and checking the format
    # Follows the correct format: username@domain.extension
    #
    # The username may contain only letters, digits, dots or the underscore character.
    #
    # The domain may contain only lowercase letters.
    #
    # The extension may contain only 2, 3 or 4 lowercase letters.
    while True:
        email = input("\nPlease enter your Email Address: ")

        # other way: (\w|\.)+@[a-z]+\.[a-z]{2,4}
        check = re.fullmatch(r"[\w.]+@[a-z]+\.[a-z]{2,4}", email)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the username and checking the format
    # Does not contain any other characters besides letters, digits or the underscore character.
    #
    # Has a minimum of 6 characters and a maximum of 12 characters.
    while True:
        user = input("\nPlease enter your Username: ")

        check = re.fullmatch(r"\w{6,12}", user)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the password and checking the format
    # Is at least 8 characters long.
    #
    # Starts with a lowercase letter.
    #
    # Should contain at least one lowercase letter, one uppercase letter, one digit and one of the following characters:
    #   $, &, ?, ! or %.
    while True:
        passw = input("\nPlease enter your Password: ")

        check = re.fullmatch(r"^[a-z](?=.{7,})(?=.*[A-Z])(?=.*\d)(?=.*[$&?!%])[a-zA-Z0-9$&?!%]+$", passw)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the credit card number and checking the format
    # The card should be issued by Visa or Mastercard only (starting with a 4 or a 5).
    #
    # It is exactly 16 digits long and contains no other characters besides digits.
    while True:
        ccnum = input("\nPlease enter your Credit Card Number (no spaces): ")

        # other way: (4|5)\d{15}
        check = re.fullmatch(r"[45][0-9]{15}", ccnum)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the credit card expiration date and checking the format
    # Is not sooner than May 2024 inclusively.
    #
    # Contains only digits and forward slashes.
    #
    # Follows the format MM/YY
    while True:
        ccdat = input("\nPlease enter your Credit Card Expiration Date (mm/yy): ")

        check = re.fullmatch(r"(0[5-9]|1[0-2])/24|(0[1-9]|1[0-2])/(2[5-9]|[3-9][0-9])", ccdat)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    # Asking the user for the credit card verification code and checking the format
    # Is a 3 digit number, does not contain any other characters.
    while True:
        cccvc = input("\nPlease enter your Credit Card Verification Code: ")

        # other way: \d{3}
        check = re.fullmatch(r"[0-9]{3}", cccvc)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break

    userinfo = ["First Name: " + fname,
                "Last Name: " + lname,
                "Date of birth: " + date,
                "Email address: " + email,
                "Username: " + user,
                "Password: " + passw,
                "Card number: " + ccnum,
                "Expiration date: " + ccdat,
                "CVC: " + cccvc]

    string = "\n".join(userinfo)

    print("This is your user account information: \n\n" + string)


def test_field():
    while True:
        string = input("\nPlease enter a string: ")

        check = re.fullmatch(r"[0-9]{3}", string)

        if check == None:
            print("Wrong format! Please try again.")
            continue
        else:
            break


if __name__ == '__main__':
    # test_field()
    validating_userinfo()
