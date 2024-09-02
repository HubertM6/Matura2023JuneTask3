from random import randrange

if __name__ == '__main__':
    with open('big_test.txt', "w") as file:
        for i in range(1000000):
            number = randrange(1, pow(2, 14))
            file.write(bin(number)[2:] + '\n')
