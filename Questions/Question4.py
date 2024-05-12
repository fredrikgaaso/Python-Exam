import random

LIST_LENGTH = 10
START = 1
END = 50
MULTIPLE = 5


def substitute(random_number):
    for i in range(LIST_LENGTH):
        if random_number[i] % MULTIPLE == 0:
            squared = random_number[i] ** 2
            random_number[i] = squared
    return random_number


def main():
    list_of_numbers = [random.randint(START, END) for i in range(LIST_LENGTH)]

    print("Before substitution, the list is:", list_of_numbers)
    print("After substitution, the list is:", substitute(list_of_numbers))


main()
