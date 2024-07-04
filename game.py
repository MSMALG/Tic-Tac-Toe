from players import Player

class XO:
    def __init__(self):
        self.board = self.board_creation()
        self.player = Player("O", "X")  #Initializing Players with symbols
    
    @staticmethod
    def board_creation():
        board = [" " for _ in range(9)]
        return board

    def printingBoard(self):
        print("\n")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("-+-" * 3)
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("-+-" * 3)
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])
        print("\n")
    
    def isEmpty(self, position):
        if self.board[position] == " ":
            return True
        return False
    
    def letterInsertion(self, letter, position):
        if self.isEmpty(position):
            self.board[position] = letter
            self.printingBoard()
        
            #Check Win Conditions 
            if self.player.WinnerCheck(self.board, letter):
                if letter == "X":
                    print("Computer wins")
                else:
                    print("Congrats You Won!")
                exit()
            
            if self.player.TieCheck(self.board):
                print("It's a Tie.")
                exit()
        
        else:
            print("Occupied Space!!!")
            #Recursive Call
            position = int(input("Enter a position for 'O' from 0 to 8: "))
            self.letterInsertion(letter, position)