def main():
    part_1()
    part_2()


def part_1():
    with open("input.txt") as file:
        safes = 0
        for line in file:
            line_array = [int(numeric_string) for numeric_string in line.strip().split(" ")]
            safes = safes + 1 if isValid(line_array) else safes
        print(f"Part1: {safes}")


def part_2():
    with open("input.txt") as file:
        safes = 0
        for line in file:
            line_array = [int(numeric_string) for numeric_string in line.strip().split(" ")]
            if isValid(line_array):
                safes += 1
            else:
                for i in range(len(line_array)):
                    copied_line = line_array.copy()
                    del(copied_line[i])
                    if isValid(copied_line):
                        safes +=1
                        break
        print(f"Part2: {safes}")


def isValid(line_array) -> bool:
    multiplier = 1 if line_array[0] < line_array[1] else -1
    diffs = [(1*multiplier), (2*multiplier), (3*multiplier)]
    for i in range (1, len(line_array)):
        if line_array[i] - line_array[i-1] not in diffs:
            return False
    return True


if __name__ == '__main__':
    main()