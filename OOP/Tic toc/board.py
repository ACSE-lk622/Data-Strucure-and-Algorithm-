from player import Player 
class Board:
    
    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
    def print_board(self):
        print("\nPositions:")
        self.print_board_with_position()

        print("Board")
        for row in self.game_board:
            print("|",end="") # show number on the same line , do not seperate it 
            for column in row :
                if column == Board.EMPTY_CELL:
                    print("   |",end="")
                else :
                    print(f" {column} |" ,end="")
            print()# already print column , need to change row
        print()# print all the rows , print new line  
    def print_board_with_position(self):
        print("|1|2|3|\n|4|5|6|\n|7|8|9|")
    
    def submit_move(self,player,move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]
        if value == Board.EMPTY_CELL :
            self.game_board[row][col] = player.marker
        else : 
            print("This position is already taken. Please enter another one ")
    def check_is_game_over(self,player,last_move):
         return ((self.check_row(player,last_move)) or (self.check_column(player,last_move)) or (self.check_diagonal(player)) or (self.check_antidiagonal(player)))
    
    def check_row(self,player,last_move):
        row_index = last_move.get_row() # which row 
        board_index = self.game_board[row_index] # the mark of row , like [0,0,"X"] 
        
        return board_index.count(player.marker) == 3 
    def check_column(self,player,last_move): # for column , this is not list 
        markers_count = 0 
        column_index =last_move.get_column()

        for i in range(3):
            if self.game_board[i][column_index] == player.marker :
                markers_count += 1
        return markers_count == 3 
    def check_diagonal(self,player):
        markers_count = 0 
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1 
        return markers_count == 3 
    def check_antidiagonal(self,player):
        markers_count = 0 
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1
        return markers_count == 3 
    
    def check_is_tie(self):
        empty_counter = 0 
        
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL) # count any 0 in the board 

        return empty_counter == 0   
    def reset_board(self):
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
#board = Board()
#player = Player()
#move1 = player.get_move()
#move2 = player.get_move()
#board.submit_move(player,move1) #give move a mark
#board.submit_move(player,move2)

#board.print_board()
#board.reset_board()
#board.print_board() # should be empty 