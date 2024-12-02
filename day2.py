import copy
from pathlib import Path

pth = Path("input/aoc_d2.txt")


def part_1(int_list: list[int], sorted_asc):
    diff_list =  [1,2,3] if sorted_asc else [-1,-2,-3] 
    for i in range(len(int_list) - 1):
        diff = int_list[i + 1] - int_list[i]
        if diff not in diff_list:
            return False
    
    return True


with open(pth, "r") as file:
    lines = file.readlines()
    lines = list(map(lambda x: x.strip("\n").split(" "), lines))
    int_lines = []
    for line in lines:
        int_lines.append([int(x) for x in line])

    part1_count = 0
    part2_count = 0
    for line in int_lines:
        sorted_asc = all(line[i] <= line[i + 1] for i in range(len(line) - 1))
        if part_1(line, sorted_asc):
            part1_count += 1


    print(f"Part 1 count: {part1_count}")
    print(f"Part 2 count: {part2_count}")