class Player:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer 
    
    def PlayerMove(self, xo):
        position = int(input("Enter a position for 'O' from 0 to 8: "))
        xo.letterInsertion(self.player, position)

    def ComputerMove(self, xo):
        OptimalScore = float("-inf")
        Move = 0

        for comp_position in range(9):
            if xo.board[comp_position] == " ":
                xo.board[comp_position] = self.computer
                score = self.MiniMax(xo.board, False)
                xo.board[comp_position] = " "

                if score > OptimalScore:
                    OptimalScore = score
                    Move = comp_position

        xo.letterInsertion(self.computer, Move)

    def MiniMax(self, board, isMax):
        if self.WinnerCheck(board, self.computer):
            return 1
        elif self.WinnerCheck(board, self.player):
            return -1
        elif self.TieCheck(board):
            return 0

        #Maximizing Player's Turn "Computer is Playing"
        if isMax:
            OptimalScore = float("-inf")
            for comp_position in range(9):
                if board[comp_position] == " ":
                    board[comp_position] = self.computer
                    score = self.MiniMax(board, False)
                    board[comp_position] = " "
                    OptimalScore = max(score, OptimalScore)
            return OptimalScore
        
        #Minimizing Player's Turn "Player is Playing"
        else:
            OptimalScore = float("inf")
            for player_pos in range(9):
                if board[player_pos] == " ":
                    board[player_pos] = self.player
                    score = self.MiniMax(board, True)
                    board[player_pos] = " "
                    OptimalScore = min(score, OptimalScore)
            return OptimalScore

    #Check if the player won or lost
    def WinnerCheck(self,board, letter):
        return (self.HorizontalCheckWin(board, letter) or 
                self.VerticalCheckWin(board, letter) or self.DiagonalCheckWin(board, letter))    
    
    #Horizontal row
    @staticmethod
    def HorizontalCheckWin(board, letter):
        if board[0] == board[1] == board[2] == letter:
            return True
        elif board[3] == board[4] == board[5] == letter:
            return True
        elif board[6] == board[7] == board[8] == letter:
            return True
        return False

    #Vertical row
    @staticmethod
    def VerticalCheckWin(board, letter):
        if board[0] == board[3] == board[6] == letter:
            return True
        elif board[1] == board[4] == board[7] == letter:
            return True
        elif board[2] == board[5] == board[8] == letter:
            return True
        return False

    #Diagonal row
    @staticmethod
    def DiagonalCheckWin(board, letter):
        if board[0] == board[4] == board[8] == letter:
            return True
        elif board[2] == board[4] == board[6] == letter:
            return True
        return False

    #Check if it is a draw
    @staticmethod
    def TieCheck(board):
        return " " not in board    
