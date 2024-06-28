test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
test_input = test_input.split(',')

inpute = open("./d15/input.txt").read().split(',')

# Part 1
ex_string = "HASH"

# convert to ASCII code -> increase count by ASCII code -> multiply count by 17 -> get modulo of value divided by 256
def hash(seq):
    count = 0
    for elem in seq:
        count += ord(elem)
        count *= 17
        count %= 256
    return count

# print(sum(map(hash, inpute)))


#Part 2
boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in inpute:
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)
        
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
            
        focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)
