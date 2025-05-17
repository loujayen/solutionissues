def solve_puzzle(clues):
    building = [[0 for _ in range(4)] for _ in range(4)]
    clues0_3 = clues[0:4]
    clues4_7 = clues[4:8]
    clues8_11 = clues[8:12][::-1]  
    clues12_15 = clues[12:16][::-1]  

    def unique(building, row, col, num):
        for i in range(4):
            if building[row][i] == num or building[i][col] == num:
                print(building)
                return False
        return True

    def check_visiblebuild_clues(building, row, col):
         # Check columns for clues0_3 and  clues8_11
        for c in range(4):
            if clues0_3[c] != 0:
                visible = 0
                max_height = 0
                for r in range(4):
                    if building[r][c] == 0:
                        break
                    if building[r][c] > max_height:
                        visible += 1
                        max_height = building[r][c]
                else:  
                    if visible != clues0_3[c]:
                        return False
            if clues8_11[c] != 0:
                visible = 0
                max_height = 0
                for r in range(3, -1, -1):
                    if building[r][c] == 0:
                        break
                    if building[r][c] > max_height:
                        visible += 1
                        max_height = building[r][c]
                else:  
                    if visible != clues8_11[c]:
                        return False
        # Check rows for clues12_15 and clues4_7
        for r in range(4):
            if clues12_15[r] != 0:
                visible = 0
                max_height = 0
                for c in range(4):
                    if building[r][c] == 0:
                        break
                    if building[r][c] > max_height:
                        visible += 1
                        max_height = building[r][c]
                else:  
                    if visible != clues12_15[r]:
                        return False
            if clues4_7[r] != 0:
                visible = 0
                max_height = 0
                for c in range(3, -1, -1):
                    if building[r][c] == 0:
                        break
                    if building[r][c] > max_height:
                        visible += 1
                        max_height = building[r][c]
                else: 
                    if visible != clues4_7[r]:
                        return False
        return True

    def retcheck(building, row, col):
        if row == 4:
            return True
        next_row = row + 1 if col == 3 else row
        next_col = col + 1 if col < 3 else 0
        if building[row][col] != 0:
            return retcheck(building, next_row, next_col)
        for num in range(1, 5):
            if unique(building, row, col, num):
                building[row][col] = num
                if check_visiblebuild_clues(building, row, col):
                    if retcheck(building, next_row, next_col):
                        return True
                building[row][col] = 0
        return False

    retcheck(building, 0, 0)
    return building

# Test the function with the example in the  issues
clues = [0, 0, 1, 2
        , 0, 2, 0, 0
        , 0, 3, 0, 0
        , 0, 1, 0, 0]
solution = solve_puzzle(clues)
for row in solution:
    print(row)