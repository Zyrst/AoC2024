from file_reader import read_a_file

lines = read_a_file("input/aoc_d4.txt")

char_list = [list(line) for line in lines]
max_position = (len(char_list[0]), len(char_list))

class Search:
    
    xmas = "XMAS"
    total_xmas = 0

    def search_grid(self, grid, position):
        
        if grid[position[1]][position[0]] != "X":
            return
        
        where_to_search = [(1, 0), (0, 1), (0, -1), (-1, 0), (1,1), (1,-1), (-1,-1), (-1,1)]
        
        for search in where_to_search:
            xy = position
            current_word = "X"
            for i in range(0, 3):
                new_pos = (xy[0] + search[0], xy[1] + search[1])
                
                if new_pos[0] < 0 or new_pos[0] >= max_position[0] or new_pos[1] < 0 or new_pos[1] >= max_position[1]:
                    break
                
                current_word += grid[new_pos[1]][new_pos[0]]
                xy = new_pos
                
            if current_word == self.xmas:
                self.total_xmas += 1
        
search = Search()
for j in range(max_position[1]):
    for i in range(max_position[0]):
        search.search_grid(char_list, (i, j))

print(search.total_xmas)