from pathlib import Path
import sys

pth = Path("input/aoc_d1_p1.txt")

with open(pth, "r") as file:
    lines = file.readlines()
    first_list = []
    second_list = []
    for line in lines:
        nums = line.split("   ")
        first_list.append(int(nums[0]))
        second_list.append(int(nums[1].removesuffix("\n")))

    first_list.sort()
    second_list.sort()

    print(f"Sum: {sum([abs(x -y) for x,y in zip(first_list, second_list)])}")
    
    occurance = 0
    for i in first_list:
        occurance += second_list.count(i) * i
    
    print(f"Occurance: {occurance}")
