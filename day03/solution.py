import re

def main():
    part_1()
    part_2()

def part_2():
    with open('input_part2.txt', 'r') as file:
        pattern = re.compile("mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)|do\(\)|don\'t\(\)")
        content = file.read().strip()
        total = 0
        can_multiply = True
        for m in re.finditer(pattern, content):
            match m.group():
                case 'do()':
                    can_multiply = True
                case "don't()":
                    can_multiply = False
                case _:
                    if (can_multiply):
                        total += int(m.group('a')) * int(m.group('b'))
        print(f"Part 2: {total}")


def part_1():
    with open('input_part1.txt', 'r') as file:
        pattern = re.compile("mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)")
        content = file.read().strip()
        total = 0
        for m in re.finditer(pattern, content):
            total += int(m.group('a')) * int(m.group('b'))
        print(f"Part 1: {total}")
        

if __name__ == '__main__':
    main()