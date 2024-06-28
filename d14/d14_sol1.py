from copy import deepcopy

def rocks():
    with open('input.txt') as f:
        lines = f.readlines()
        grid = []
        row = 0
        for line in lines:
            if line.strip() == '':
                continue
            else:
                col = 0
                extracted = []
                for char in line.strip():
                    extracted.append(char)
                    col +=1
                grid.append(extracted)
            row+=1
        transposed_grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        for i in range(len(transposed_grid)):
            last = []
            whole_row = []
            for j in range(len(transposed_grid[i])):
                if transposed_grid[i][j] == '#':
                    if len(last) > 0:
                        new_row = move_rocks(deepcopy(last))
                        whole_row = whole_row + new_row + ['#']
                        last = []
                    else:
                        whole_row = whole_row + ['#']
                else:
                    last.append(transposed_grid[i][j])
            if len(last) > 0:
                new_row = move_rocks(deepcopy(last))
                whole_row = whole_row + new_row
            transposed_grid[i] = whole_row
        
        grid = [[transposed_grid[j][i] for j in range(len(transposed_grid))] for i in range(len(transposed_grid[0]))]
        total = count_grid(grid)
        print(total)        
        
    return

def move_rocks(row:list):
    if len(set(row)) == 1:
        return row
    else:
        return row.count('O') * ['O'] + row.count('.') * ['.']

def count_grid(grid):
    total = 0
    for i in range(len(grid),0,-1):
        total += i * grid[len(grid)-i].count('O')
    return total

def rocks_variant():
    with open('input.txt') as f:
        lines = f.readlines()
        grid = []
        row = 0
        for line in lines:
            if line.strip() == '':
                continue
            else:
                col = 0
                extracted = []
                for char in line.strip():
                    extracted.append(char)
                    col +=1
                grid.append(extracted)
            row+=1
        original_grid = deepcopy(grid)
        cycle_nb, precycle = find_cycle(grid)
        grid = original_grid
        for i in range(precycle):
            grid = cycle_once(grid)
        for i in range((1000000000 - precycle) % (cycle_nb-precycle)):
            grid = cycle_once(grid)
        total = count_grid(grid)
        print(total)        
        
    return

def cycle_once(grid):
    grid = tilt(grid,'north')
    grid = tilt(grid,'west')
    grid = tilt(grid,'south')
    grid = tilt(grid,'east')
    return grid

def find_cycle(grid):
    seen = []
    found = False
    count = 0
    while not found:
        grid = deepcopy(cycle_once(grid))
        if grid in seen:
            cycle_index = seen.index(grid)
            found = True
        else:
            seen.append(grid)
        count += 1 
    return count, cycle_index + 1
def print_grid(grid):
    for row in grid:
        temp = ''
        for c in row:
            temp += c
        print(temp)
    return

def tilt(grid,direction):
    if direction == 'north':
        transposed_grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    elif direction == 'west':
        transposed_grid = deepcopy(grid)
    elif direction == 'south':
        transposed_grid = grid[::-1]
        transposed_grid = [[transposed_grid[j][i] for j in range(len(transposed_grid))] for i in range(len(transposed_grid[0]))]
    else:
        transposed_grid = [e[::-1] for e in grid]
    for i in range(len(transposed_grid)):
        last = []
        whole_row = []
        for j in range(len(transposed_grid[i])):
            if transposed_grid[i][j] == '#':
                if len(last) > 0:
                    new_row = move_rocks(deepcopy(last))
                    whole_row = whole_row + new_row + ['#']
                    last = []
                else:
                    whole_row = whole_row + ['#']
            else:
                last.append(transposed_grid[i][j])
        if len(last) > 0:
            new_row = move_rocks(deepcopy(last))
            whole_row = whole_row + new_row
        transposed_grid[i] = whole_row
    
    if direction == 'north':
        return [[transposed_grid[j][i] for j in range(len(transposed_grid))] for i in range(len(transposed_grid[0]))]
    elif direction == 'west':
        return transposed_grid
    elif direction == 'south':
        transposed_grid = [[transposed_grid[j][i] for j in range(len(transposed_grid))] for i in range(len(transposed_grid[0]))]
        return transposed_grid[::-1]
    else:
        return [e[::-1] for e in transposed_grid]


if __name__ == '__main__':
    rocks()
    rocks_variant()