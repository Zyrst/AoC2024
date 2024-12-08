from collections import defaultdict
from file_reader import read_a_file

lines = read_a_file("input/aoc_d5.txt")

class Instructions:
    def __init__(self, line: str) -> None:
        self.instructions = [int(l) for l in line.strip("\n").split(",")]

break_index = 0
test_page = defaultdict(set)

for i, line in enumerate(lines):
    if line == "\n":
        break_index = i
        break
    
    x,y = line.split("|")
    x = int(x)  # Must before y
    y = int(y)
    test_page[y].add(x)


inst: list[Instructions] = []
while break_index <= len(lines) - 2:
    break_index += 1
    inst.append(Instructions(lines[break_index]))

correct_rulings: list[Instructions] = []
answer = 0
for instruction in inst:
    current_section = []
    ok = True
    for i, instruction_page in enumerate(instruction.instructions):
        for j, inst_page in enumerate(instruction.instructions):
            if i < j and inst_page in test_page[instruction_page]:
                ok = False
    
    if ok:
        answer += instruction.instructions[len(instruction.instructions) // 2]


print(answer)