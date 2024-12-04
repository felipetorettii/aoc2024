def main():
    part_1()
    part_2()

def part_1():
    left = []
    right = []
    with open("input.txt") as file:
        for line in file:
            splitted_numbers = line.strip().split("   ")
            left.append(int(splitted_numbers[0]))
            right.append(int(splitted_numbers[1]))
        left.sort()
        right.sort()
        sum_of_distance = 0
        for i in range(len(left)):
            sum_of_distance += abs((left[i] - right[i]))
        print(f'Part 1: {sum_of_distance}')

def part_2():
    left = []
    right = []
    with open("input.txt") as file:
        for line in file:
            splitted_numbers = line.strip().split("   ")
            left.append(int(splitted_numbers[0]))
            right.append(int(splitted_numbers[1]))
    similarity_score = 0
    for i in range(len(left)):
        left_occurrences = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                left_occurrences += 1
            if (j == len(right)-1):
                similarity_score += left_occurrences * left[i]
    print(f'Part 2: {similarity_score}')



            

if __name__ == '__main__':
    main()