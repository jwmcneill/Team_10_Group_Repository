'''
Code created by Mike Horn - Team 10
Asks for the year of birth to calculate retirement age, or
checks for end-of-program input ('')
'''


def ask_birth_year():
    valid_response = False
    while not valid_response:
        year = input("Enter the year of birth: ")
        # input signals to terminate program, end loop
        if year == '':
            valid_response = True
        else:
            year = int(year)
            # check for valid input
            if 1900 <= year <= 2020:
                valid_response = True

    return year

'''
Asks for the month of birth to calculate retirement age
'''
def ask_birth_month():
    valid_response = False
    while not valid_response:
        month = int(input("Enter the month of birth (ex: 8 for August): "))
        # check if valid  input
        if 1 <= month <= 12:
            valid_response = True
    return month

'''
Calculates retirement age from given birth year based on the government
website and guidelines. Age is returned as a tuple. 
'''
def calc_retirement_age(birth_year):
    if birth_year <= 1937:
        age = 65, 0
    elif birth_year <= 1942:
        age = 65, (birth_year - 1937) * 2
    elif birth_year <= 1954:
        age = 66, 0
    elif birth_year <= 1959:
        age = 66, (birth_year - 1954) * 2
    else:
        age = 67, 0
    return age

'''
Calculates retirement date (month and year) 
from the birth date and retirement age.
'''
def calc_retirement_date(birth_date, retirement_age):
    retirement_year = birth_date[0] + retirement_age[0]
    retirement_month = birth_date[1] + retirement_age[1]
    # check if more than 12 months in year, adjust accordingly
    if retirement_month > 12:
        retirement_year = retirement_year + 1
        retirement_month = retirement_month - 12
    # get string representation of month
    retirement_month = month_to_string(retirement_month)
    return retirement_year, retirement_month

'''
Returns a string of the month from a digit 1 through 12. 
'''
def month_to_string(month_num):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
              6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
              11: 'November', 12: 'December'}

    return months[month_num]


def main():
    calculator_on = True

    while calculator_on:
        birth_year = ask_birth_year()
        # calculator off, user input = ''
        if birth_year == '':
            calculator_on = False;
        else:
            birth_date = (birth_year, ask_birth_month())

            # calculate retirement age and print
            retirement_age = calc_retirement_age(birth_date[0])
            print(f"Your full retirement age is {retirement_age[0]} "
                  f"and {retirement_age[1]} months.")

            # calculate retirement date and print
            retirement_date = calc_retirement_date(birth_date, retirement_age)
            print(f"This will be in {retirement_date[1]} of {retirement_date[0]}\n")


if __name__ == "__main__":
    main()