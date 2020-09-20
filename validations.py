
#Group 7
#Karla Aguirre
#Hugo Salvador Hernandez
#Xing Liu
#Validations for year and month on FullRetirementAge program


def validationYear(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1900 or user_input > 3000:
                raise ValueError
        except ValueError:
            print("Please enter numeric values for year between 1900 and 3000")
            continue

        else:

            break
    return user_input


def validationMonth(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1 or user_input > 12:
                raise ValueError
        except ValueError:
            print("Please enter numeric values for month between 1 and 12")
            continue

        else:

            break
    return user_input
