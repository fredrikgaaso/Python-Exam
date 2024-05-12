"""
The task assumes that the user does not enter invalid inputs,
therefore we have chosen not to include a try except or an else statement
"""

def main():
    positive_number = []
    negative_number = []
    zeros = []

    while True:
        user_input = input("Enter an integer number (blank to quit): ")
        if user_input == "":
            break
        elif int(user_input) == 0:
            zeros.append(user_input)
        elif int(user_input) > 0:
            positive_number.append(user_input)
        elif int(user_input) < 0:
            negative_number.append(user_input)

    all_numbers = ', '.join(positive_number + zeros + negative_number)
    print(all_numbers)


main()
