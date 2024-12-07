DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    part_1()
    part_2()

def part_1():
    with open("day06/input.txt", "r") as file:
        lines_array = []
        for idx, line in enumerate(file):
            current_line_list = list(line.strip())
            if ('^' in current_line_list):
                guard_x = current_line_list.index('^')
                guard_y = idx
            lines_array.append(current_line_list)
    directions_behavior = {
        '^': {'y': -1, 'x': 0, 'flip': '>'},
        '>': {'y': 0, 'x': 1, 'flip': 'v'},
        'v': {'y': 1, 'x': 0, 'flip': '<'},
        '<': {'y': 0, 'x': -1,'flip': '^'}
    }
    guard_original_path = []
    while True:
        guard_pointing = lines_array[guard_y][guard_x]
        guard_behavior = directions_behavior[guard_pointing]
        next_y, next_x = guard_y + guard_behavior['y'], guard_x + guard_behavior['x']        

        try:
            guard_next_pos = lines_array[next_y][next_x]
        except:
            guard_original_path.append([guard_y, guard_x])
            break

        if (guard_next_pos == '#'):
            guard_pointing = guard_behavior['flip']
            lines_array[guard_y][guard_x] = guard_pointing
            continue
        if (guard_next_pos != 'X'):
            guard_original_path.append([guard_y, guard_x])
        lines_array[guard_y][guard_x], lines_array[next_y][next_x] = 'X', guard_pointing
        guard_y, guard_x = next_y, next_x
    print(f'Part 1: {len(guard_original_path)}')


def part_2():
    with open("day06/input.txt", "r") as file:
        lines = []
        line = file.readline().removesuffix("\n")
        while line != '':
            lines.append(line)
            line = file.readline().removesuffix("\n")
    lines = list(map(lambda s: [x for x in s], lines))
    n, m = len(lines), len(lines[0])
    i, j = get_guard_coords(lines)
    curr_dir = 0
    di, dj = DIR[0]
    visited = set()
    obstacles_that_make_loops = 0
    while 0 <= i < n and 0 <= j < m:
        visited.add((i, j))
        
        ni, nj = i + di, j + dj
        if not(0 <= ni < n and 0 <= nj < m):
            break

        while lines[ni][nj] == '#':
            curr_dir = (curr_dir + 1) % len(DIR)
            di, dj = DIR[curr_dir]
            ni, nj = i+di, j+dj
        
        if (ni, nj) not in visited and check_loop(curr_dir, (ni, nj), lines):
            obstacles_that_make_loops += 1
        
        i, j = ni, nj
        
    print(f'Part 2: {obstacles_that_make_loops}')


def get_guard_coords(lines: list[str]) -> tuple[int, int]:
    for i, row in enumerate(lines):
        for j, val in enumerate(row):
            if val == '^':
                return i, j  

    return -1, -1

def check_loop(curr_dir: int, obstacle: tuple[int, int], maze: list[str]) -> bool:
  n, m = len(maze), len(maze[0])
  
  oi, oj = obstacle
  di, dj = DIR[curr_dir]
  i, j = oi-di, oj-dj
  
  maze[oi][oj] = '#'
  visited = set()
  
  while 0 <= i < n and 0 <= j < m:
    if (i, j, curr_dir) in visited:
      maze[oi][oj] = '.'
      return True
      
    visited.add((i, j, curr_dir))
    
    ni, nj = i+di, j+dj
    if not(0 <= ni < n and 0 <= nj < m):
      break 
    
    while maze[ni][nj] == '#':
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    i, j = ni, nj
  
  maze[oi][oj] = '.'
  return False
        


if __name__ == '__main__':
    main()