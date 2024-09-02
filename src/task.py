def read_file(path):
    binary_numbers = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            binary_numbers.append(line.strip())
    return binary_numbers


def task_one(path):
    binary_numbers = read_file(path)
    number_of_sustainable = len(list(filter(lambda n: n.count('1') == n.count('0'), binary_numbers)))
    number_of_nearly_sustainable = len(list(filter(lambda n: abs(n.count('1') - n.count('0')) == 1, binary_numbers)))
    return number_of_sustainable, number_of_nearly_sustainable


def task_two(path):
    binary_numbers = list(filter(lambda n: len(n) == 8 and 4 <= n.count('1') <= 5, read_file(path)))
    return binary_numbers


def task_three(path):
    binary_numbers = read_file(path)
    max_difference = 0
    for i in range(1, len(binary_numbers)):
        difference = abs(int(binary_numbers[i], 2) - int(binary_numbers[i - 1], 2))
        max_difference = max(difference, max_difference)
    return str(bin(max_difference))[2:]


def has_zero(number):
    return str(number).count('0') > 0


def sum_of_different_digits(number):
    return sum(map(lambda n: int(n), set(str(number))))


def task_four(path):
    binary_numbers = read_file(path)
    decimal_numbers = list(map(lambda n: int(n, 2), binary_numbers))
    number_without_zero = len(list(filter(lambda n: not has_zero(n), decimal_numbers)))
    best_number = decimal_numbers[0]
    for number in decimal_numbers:
        if sum_of_different_digits(number) > sum_of_different_digits(best_number):
            best_number = number
    return number_without_zero, best_number


if __name__ == '__main__':
    print(task_four('big_test.txt'))
