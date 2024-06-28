inpute = open("./input.txt").read()

# Imports
import numpy as np
from multiprocessing import Pool
import multiprocess as mp

# Split on new lines
lines = inpute.split('\n')

# Initialize a dictionary to store each section data
seeds_nb = []
section_data = {}

# Function to process a section and extract numbers
def process_section(section_lines):
    section_data = []
    for line in section_lines:
        numbers = [int(num) for num in line.split() if num.isdigit()]
        section_data.append(numbers)
    return section_data

# Iterate through each line and process the corresponding section
current_section = None
for line in lines:
    if line:
        if ':' in line:
            current_section = line.split(':')[0].strip()
            if current_section == 'seeds':
                seeds_nb.extend(int(num) for num in line.split(':')[1].strip().split(' ') if num.isdigit())
                #section_data[current_section] = [int(num) for num in line.split(':')[1].strip().split(' ') if num.isdigit()]
            else:
                section_data[current_section] = []
        else:
            section_data[current_section].extend(process_section([line]))

seeds_nbp = np.array(seeds_nb)

seeds_new = np.array([])

def process_seed(seed):
    seeds_map[seed] = seed
    
    for key, value in section_data.items():
        for line in section_data[key]:
                if seeds_map[seed] in range(line[1], line[1]+line[2]):
                    seeds_map[seed] = seeds_map[seed]+(line[0]-line[1])
                    break

    return seeds_map[seed]

for i in range(0, len(seeds_nbp)-1, 2):
    for j in range(seeds_nbp[i], seeds_nbp[i]+seeds_nbp[i+1], 100000):
        seeds_new = np.concatenate((seeds_new, np.array([j])))

seeds_map = {}

for seed in seeds_new:
    seeds_map[seed] = seed

with mp.Pool(15) as pool:
    final_seeds_2 = pool.map(process_seed, seeds_new)

min(final_seeds_2)