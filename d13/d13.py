"""
 inspired by -- https://www.youtube.com/watch?v=GYbjIvTQ_HA&ab_channel=HyperNeutrino
"""

def find_mirror(grid, part):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if part == 1 and above == below:
                return r
        elif part == 2 and sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
                return r
        
    return 0

def compute(part):
    total = 0

    for block in open("./input.txt").read().split("\n\n"):
        grid = block.splitlines()

        row = find_mirror(grid, part)
        total += row * 100

        col = find_mirror(list(zip(*grid)), part)
        total += col

    print(total)


compute(2)