from board import Board  
from player import Player  
class TicTacToeGame:
    def start(self):
        print("*****************************")
        print(" Welcome  to   Tic-Tac-Toe    ")
        print("*****************************")

        board = Board()
        player = Player()
        computer = Player(False)
        
        board.print_board()

        #Ask the user if he/she would like to player another round 
        while True :#game logic
            #Get move , check tie , check game over 
            while True :#round 

                player_move = player.get_move() 
                board.submit_move(player,player_move) # put move reference in argument 
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie! Try again")
                    break
                elif board.check_is_game_over(player,player_move):
                    print("Awesome. You won the game!")
                    break
                else : #it's computer turn to move 
                    computer_move = computer.get_move()
                    board.submit_move(computer,computer_move)
                    board.print_board()
                    # check computer win or not 
                    if board.check_is_game_over(computer,computer_move):
                        print("Oops... The computer won . Try again !")
                        break 
            
            player_again = input("Would you like to player again ? Enter X for Yes or O for NO").upper()    

            if player_again  == "O":
                print("Bye ! Come back soon ")
                break
            elif player_again == "X":
                self.start_new_round(board)
            else :
                print("Your input was not valid but I assum you want to play")
                self.start_new_round(board)
            
    def start_new_round(self,board):
        print("*****************************")
        print("         New round      ")
        print("*****************************")

        board.reset_board()
        board.print_board()
game = TicTacToeGame()
game.start()