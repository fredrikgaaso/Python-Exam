import random

LIST_LENGTH = 10
START = 1
END = 50


def main():
    randomNumber = [random.randint(START, END) for i in range(LIST_LENGTH)]
    print(randomNumber)

    def substitute():
        for i in range(LIST_LENGTH):
            if randomNumber[i] % 5 == 0:
                var = randomNumber[i] ** 2
                randomNumber[i] = var
        print(randomNumber)

    substitute()


main()
