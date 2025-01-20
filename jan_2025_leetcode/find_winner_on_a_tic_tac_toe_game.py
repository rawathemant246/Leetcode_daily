from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        
        
        def check_winner(grid):
            
            for row in grid:
                if row[0] == row[1] == row[2] and row[0] != ' ':
                    return row[0]
            
            
            for col in range(3):
                if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
                    return grid[0][col]
            
            
            if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
                return grid[0][0]
            
            
            if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
                return grid[0][2]
            
            return None

        
        for i, move in enumerate(moves):
            row, col = move
            
            
            if i % 2 == 0:      # yeh index idea aaise kaam krta hai ki [0,0],[2,0],[1,1],[2,1],[2,2]  index 0 pe move [0,0] hai toh 0%2 = 0 so 'X' move
                grid[row][col] = 'X'
            else:  
                grid[row][col] = 'O'
            
            # Check if there's a winner after this move
            winner = check_winner(grid)
            if winner:
                return 'A' if winner == 'X' else 'B'
        
        # If all moves are played and no winner, it's a draw
        if len(moves) == 9:
            return 'Draw'
        
        # If the game is still ongoing
        return 'Pending'

if __name__ == "__main__":
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    sol = Solution()
    print(sol.tictactoe(moves))