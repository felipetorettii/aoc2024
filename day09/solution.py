def main():
    part_1()

def part_1():
    with open('day09/input.txt', 'r') as file:
        line = file.read()
    blocks = []
    file_index = 0
    for i, x in enumerate(line):
        x = int(x)
        if (i % 2 == 0):
            blocks += [file_index] * x
            file_index += 1
        else:
            blocks += ['.'] * x
    
    first_dot = 0
    last_number = len(blocks) - 1
    while last_number > first_dot:
        while blocks[first_dot] != '.':
            first_dot += 1
        while blocks[last_number] == '.':
            last_number -= 1
        if (first_dot > last_number):
            break
        blocks[first_dot], blocks[last_number] = blocks[last_number], blocks[first_dot]
    total = 0
    for i, block in enumerate(blocks):
        if (block == '.'):
            break
        total += i * int(block)
    print(total)

if __name__ == '__main__':
    main()