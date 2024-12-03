import re
from file_reader import read_a_file

lines = read_a_file("input/aoc_d3.txt")

# (mul\()[0-9]*[,][0-9]*\)
list_lines = []
for line in lines:
    result = re.findall("(mul\([0-9]*,[0-9]*\))", line)
    for group in result:
        res = re.search("([0-9]*),([0-9]*)", group)
        list_lines.append(int(res.group(1)) * int(res.group(2)))

print(sum(list_lines))