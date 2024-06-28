"""
 inspired by -- https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day10p1.py
"""

from collections import deque

grid = ["..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ..."]

# Get starting position and elems next to it
starting = (0,0)
start_char = {}

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "S":
            starting = (i,j)
            
            up = grid[i-1][j]
            right = grid[i][j+1]
            down = grid[i+1][j]
            left = grid[i][j-1]
            
            if up == '|' or up == '7' or up == 'F':
                start_char['up'] = up
            if right == '-' or right == 'J' or right == '7':
                start_char['right'] = right
            if down == '|' or down == 'L' or down == 'J':
                start_char['down'] = down
            if left == '-' or left == 'F' or left == 'L':
                start_char['left'] = left
                
            break
            
sr, sc = starting[0], starting[1]

# Get value of S
first_val = ''

if 'right' in start_char.keys() and 'down' in start_char.keys():
    first_val = 'F'
elif 'right' in start_char.keys() and 'up' in start_char.keys():
    first_val = 'L'
elif 'right' in start_char.keys() and 'left' in start_char.keys():
    first_val = '-'
elif 'up' in start_char.keys() and 'down' in start_char.keys():
    first_val = '|'
elif 'up' in start_char.keys() and 'left' in start_char.keys():
    first_val = 'J'
elif 'left' in start_char.keys() and 'down' in start_char.keys():
    first_val = '7'

# Solve part 1
loop = {(sr, sc)}
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]

    if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in loop:
        loop.add((r - 1, c))
        q.append((r - 1, c))
        
    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
        loop.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
        loop.add((r, c - 1))
        q.append((r, c - 1))

    if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
        loop.add((r, c + 1))
        q.append((r, c + 1))

print("Part 1: ", len(loop) // 2)

# Solve part 2
grid = [row.replace("S", first_val) for row in grid]
grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

outside = set()

for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal): {ch}")
        if not within:
            outside.add((r, c))
            
print("Part 2: ", len(grid) * len(grid[0]) - len(outside | loop))