from game import XO

def main():
    game = XO()

    user_decision = input("Do you want to start first or the computer? Type 'me' if you want to begin first or 'co' for the computer \n")
    try:
        if user_decision == "me":
            current_player = "player"
        elif user_decision == "co":
            current_player = "computer"
        else:
            raise ValueError("Enter as INSTRUCTED!!!")
        
    except ValueError as ve:
        print(ve)
        exit()
    
    
    while True:
        if current_player == "player":
            game.player.PlayerMove(game)
            current_player = "computer"
        else:
            game.player.ComputerMove(game)
            current_player = "player"


if __name__ == "__main__":
    main()
