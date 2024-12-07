from itertools import product
from operator import add, mul

def main():
    sol(False)
    sol(True)


def concat(a, b):
    return int(str(a) + str(b))


def sol(part_2: bool):
    operators = {add, mul, concat} if part_2 else {add, mul}
    total = 0
    with open('day07/input.txt', 'r') as file:
        for line in file:
            equation = line.strip().split(':')
            result, numbers = int(equation[0]), [int(number) for number in equation[1].strip().split(" ")]
            operator_combinations = generate_combinations(operators, len(numbers)-1)
            for combination in operator_combinations:
                combination_result = numbers[0]
                for i, operator in enumerate(combination):
                    combination_result = operator(combination_result, numbers[i+1])
                
                if combination_result == result:
                    total += result
                    break
    print(total)

def generate_combinations(operators, length):
    return list(product(operators, repeat=length))


if __name__ == '__main__':
    main()