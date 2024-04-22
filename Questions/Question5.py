def main():
    positive_number = []
    negative_number = []
    zeros = []

    while True:
        user_input = input("Enter an integer number (blank to quit): ")
        if user_input == "":
            break
        if int(user_input) == 0:
            zeros.append(user_input)
        if int(user_input) > 0:
            positive_number.append(user_input)
        if int(user_input) < 0:
            negative_number.append(user_input)
    print(positive_number + zeros + negative_number)

main()
