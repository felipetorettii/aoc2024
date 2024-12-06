from functools import cmp_to_key

def main():
    part_1()
    part2()

def part2():
  p1, p2 = open('day05/input.txt').read().split('\n\n')
  rules = [tuple(line.split('|')) for line in p1.splitlines()]
  updates = (line.split(',') for line in p2.splitlines())

  def compare(a, b):
    return -1 if (a, b) in rules else 1 if (b, a) in rules else 0

  total = 0
  for update in updates:
    new = sorted(update, key=cmp_to_key(compare))
    if (new != update):
      total += int(new[len(new) // 2])

  print(f'Part 2: {total}')


def part_1():
    file_name = 'day05/input.txt'
    with open(file_name, 'r') as file:
        rules_map: dict[int, list[int]] = {}
        update_list: list[list[int]] = []
        mounting_rules = True
        for line in file:
            splitted_numbers = line.strip().split("|")
            if line == '\n':
                mounting_rules = False
                continue
            if (mounting_rules):
                add_to_rules_map(rules_map, int(splitted_numbers[1]), int(splitted_numbers[0]))
            else:
                update_list.append([int(numeric_string) for numeric_string in line.strip().split(",")])
        sum_of_correct = 0
        for update in update_list: #update [97,13,75,29,47]
            is_update_valid = True
            for page_index, page in enumerate(update): #page 97..13..75..29..47
                if not is_update_valid:
                    break
                if page in rules_map: # 47 tem regra? tem, as regras são 97 e 75
                    for rule in rules_map[page]: # Itera entre 97 e 75 e precisa ver se tem na linha de update
                        if rule in update:
                            is_update_valid = update.index(rule) < page_index
                        if not is_update_valid:
                            break
            sum_of_correct += update[len(update)//2] if is_update_valid else 0
        print(f'Part 1: {sum_of_correct}')
                            



            

def add_to_rules_map(map: dict[int, list[int]], key: int, value: int) -> dict:
    if key not in map:
        map[key] = []
    if value not in map[key]:
        map[key].append(value)


if __name__ == '__main__':
    main()