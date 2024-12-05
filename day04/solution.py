def main():
    part_1()
    part_2()

def part_2():
    file_name = 'day04/input_part02.txt'
    lines = get_lines_array(file_name)
    count = 0
    for line_index, line in enumerate(lines):
        for letter_idx, letter in enumerate(line):
            if (letter == 'M'):
                count += check_for_masx(lines, letter_idx, line_index, line)
    print(f"Part 2: {count}")


def part_1():
    file_name = 'day04/input_part01.txt'
    lines = get_lines_array(file_name)
    count = 0
    for line_index, line in enumerate(lines):
        for letter_idx, letter in enumerate(line):
            if (letter == 'X'):
                count += check_for_xmas(line, letter_idx, 1, line_index, lines, None)
    print(f"Part 1: {count}")

# MA
def check_for_masx(lines: list[list[str]], letter_idx: int, line_index: int, line: list[str]):
    sum_found = 0
    can_check_right = True if letter_idx + 2 < len(line) else False
    can_check_left = True if letter_idx - 2 >= 0 else False
    can_check_down = True if line_index + 2 < len(lines) else False
    can_check_up = True if line_index - 2 >= 0 else False
    if can_check_right and can_check_down:
        if line[letter_idx + 2] == 'S' and lines[line_index+1][letter_idx+1] == 'A' and \
            lines[line_index+2][letter_idx] == 'M' and lines[line_index+2][letter_idx+2] == 'S':
            print(f'achou line index {line_index} letter index {letter_idx}')
            sum_found += 1
        if line[letter_idx + 2] == 'M' and lines[line_index+1][letter_idx+1] == 'A' and \
            lines[line_index+2][letter_idx] == 'S' and lines[line_index+2][letter_idx+2] == 'S':
            print(f'achou line index {line_index} letter index {letter_idx}')
            sum_found += 1
    if can_check_right and can_check_up:
        if line[letter_idx + 2] == 'M' and lines[line_index-1][letter_idx+1] == 'A' and \
            lines[line_index-2][letter_idx] == 'S' and lines[line_index-2][letter_idx+2] == 'S':
            print(f'achou line index {line_index} letter index {letter_idx}')
            sum_found += 1
    if can_check_left and can_check_down:
        if line[letter_idx - 2] == 'S' and lines[line_index+1][letter_idx-1] == 'A' and \
            lines[line_index+2][letter_idx] == 'M' and lines[line_index+2][letter_idx-2] == 'S':
            print(f'achou line index {line_index} letter index {letter_idx}')
            sum_found += 1

    return sum_found
        

def check_for_xmas(line: list[str], letter_idx: int, word_index: int, current_line: int, lines: list[list[str]], direction) -> int:
    found_word = 0
    number_of_lines = len(lines)
    if word_index == 4:
        return 1
    word = ['X', 'M', 'A', 'S']

    can_go_right = len(line) > (letter_idx + word_index)
    can_go_left = (letter_idx - word_index) >= 0
    can_go_up = (current_line - 1) >= 0
    can_go_down = (current_line + 1) < number_of_lines
    can_go_up_left = can_go_up and can_go_left
    can_go_up_right = can_go_up and can_go_right
    can_go_down_left = can_go_down and can_go_left
    can_go_down_right = can_go_down and can_go_right 

    if can_go_right and line[letter_idx + word_index] == word[word_index] and (direction is None or direction == "RIGHT"):
        found_word += 1 if check_for_xmas(line, letter_idx, word_index+1, current_line, lines, "RIGHT") else 0
    if can_go_left and line[letter_idx - word_index] == word[word_index] and (direction is None or direction == "LEFT"):
        found_word += 1 if check_for_xmas(line, letter_idx, word_index+1, current_line, lines, "LEFT") else 0
    if can_go_up and lines[current_line - 1][letter_idx] == word[word_index] and (direction is None or direction == "UP"):
        found_word += 1 if check_for_xmas(lines[current_line - 1], letter_idx, word_index+1, current_line - 1, lines, "UP") else 0
    if can_go_down and lines[current_line + 1][letter_idx] == word[word_index] and (direction is None or direction == "DOWN"):
        found_word += 1 if check_for_xmas(lines[current_line + 1], letter_idx, word_index+1, current_line + 1, lines, "DOWN") else 0
    if can_go_up_left and lines[current_line - 1][letter_idx - word_index] == word[word_index] and (direction is None or direction == "UP_LEFT"):
        found_word += 1 if check_for_xmas(lines[current_line - 1], letter_idx, word_index+1, current_line - 1, lines, "UP_LEFT") else 0
    if can_go_up_right and lines[current_line - 1][letter_idx + word_index] == word[word_index] and (direction is None or direction == "UP_RIGHT"):
        found_word += 1 if check_for_xmas(lines[current_line - 1], letter_idx, word_index+1, current_line - 1, lines, "UP_RIGHT") else 0
    if can_go_down_left and lines[current_line + 1][letter_idx - word_index] == word[word_index] and (direction is None or direction == "DOWN_LEFT"):
        found_word += 1 if check_for_xmas(lines[current_line + 1], letter_idx, word_index+1, current_line + 1, lines, "DOWN_LEFT") else 0
    if can_go_down_right and lines[current_line + 1][letter_idx + word_index] == word[word_index] and (direction is None or direction == "DOWN_RIGHT"):
        found_word += 1 if check_for_xmas(lines[current_line + 1], letter_idx, word_index+1, current_line + 1, lines, "DOWN_RIGHT") else 0
        
    return found_word

def get_lines_array(file_name: str) -> list[str]:
    lines_array = []
    with open(file_name) as file:
        for line in file:
            lines_array.append(list(line.strip()))
    return lines_array


if __name__ == '__main__':
    main()