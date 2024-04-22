import random


def main():
    randomNumber = [random.randint(1, 50) for i in range(10)]
    print(randomNumber)

    def substitute():
        for i in range(10):
            if randomNumber[i] % 5 == 0:
                var = randomNumber[i] * randomNumber[i]
                randomNumber[i] = var
        print(randomNumber)

    substitute()


main()
