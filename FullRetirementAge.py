#Group 7
#Karla Aguirre
#Hugo Salvador Hernandez
#Xing Liu
#main

from validations import *
#import funtions to validate user input


def main():
    year = validationYear("Please enter your birth year ")
    month = validationMonth("Please enter your birth month ")
    age_normal_retirement, year_full_retirement, month_full_retirement = normal_retirement(year, month)
    final_month = month_string(month_full_retirement)
    print("Your full retirement age is: ", age_normal_retirement)
    print("This will be in: ", final_month, " of ", year_full_retirement)


def normal_retirement(year, month):
    retirement_year = 0
    retirement_month = month
    age = " "
    if year <= 1937:
        age = "65 and 0 months"
        retirement_year = year + 65
    elif year == 1938:
        age = "65 and 2 months"
        retirement_year = year + 65
        retirement_month = month + 2
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1939:
        age = "65 and 4 months"
        retirement_year = year + 65
        retirement_month = month + 4
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1940:
        age = "65 and 6 months"
        retirement_year = year + 65
        retirement_month = month + 6
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1941:
        age = "65 and 8 months"
        retirement_year = year + 65
        retirement_month = month + 8
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1942:
        age = "65 and 10 months"
        retirement_year = year + 65
        retirement_month = month + 10
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif 1943 <= year <= 1954:
        age = "66 and 0 months"
        retirement_year = year + 66
    elif year == 1955:
        age = "66 and 2 months"
        retirement_year = year + 66
        retirement_month = month + 2
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1956:
        age = "66 and 4 months"
        retirement_year = year + 66
        retirement_month = month + 4
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1957:
        age = "66 and 6 months"
        retirement_year = year + 66
        retirement_month = month + 6
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1958:
        age = "66 and 8 months"
        retirement_year = year + 66
        retirement_month = month + 8
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year == 1959:
        age = "66 and 10 months"
        retirement_year = year + 66
        retirement_month = month + 10
        if retirement_month > 12:
            retirement_year = retirement_year + 1
            retirement_month = retirement_month - 12
    elif year >= 1960:
        age = "67 and 0 months"
        retirement_year = year + 67
    return age, retirement_year, retirement_month


def month_string(month):
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"
    return month


if __name__ == "__main__":
	main()






