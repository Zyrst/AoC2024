from file_reader import read_a_file

map = read_a_file("input/aoc_d6.txt")
map = [list(m) for m in map]
position = (0, 0)
facing = (0, -1)

for i, m in enumerate(map):
    for j, x in enumerate(m):
        if x == "^":
            position = (j, i)
            break

dict_steps = {}
while True:
    x = position[0] + facing[0]
    y = position[1] + facing[1] 
    
    if x < 0 or x >= len(map[0])\
        or y < 0 or y >= len(map):
        break
    
    if map[y][x] == "#":
        match facing:
            case (0, -1):
                facing = (1, 0)
            case (1, 0):
                facing = (0, 1)
            case (0, 1):
                facing = (-1, 0)
            case (-1, 0):
                facing = (0, -1)
    else:
        position = (x, y)
        dict_steps[position] = "X"


print(len(dict_steps))