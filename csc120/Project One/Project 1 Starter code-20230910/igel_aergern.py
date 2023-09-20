
import igel_view as view

PLAYER_COUNT = 4
COLORS = ['Y', 'R', 'G', 'P', 'B', 'O']

def run_game():
    """Runs one full game of Igel Aergern."""
    # *** Do NOT modify this function ***
    players = create_players(PLAYER_COUNT)
    b = create_board()
    update_interface(b)
    start_up_phase(b, players)
    main_phase(b, players)

def create_players(num):
    # *** create list of num players ***
    return []

def create_board():
    # *** create empty board ***
    return None

def update_interface(igel_board):
    b_str = "" # *** string representation of igel_board ***
    view.refresh_view(b_str)

def start_up_phase(b, players):
    # *** Run start up phase of the game where players place their Igel tokens on the board. ***
    pass

def main_phase(b, players):
    # *** Run main phase of the game where players roll the die, potentially move 
    # one of their tokens sideways, and move a token forward. This phase ends 
    # when one player has won. ***
    pass
  


############
### Main ###

if __name__=='__main__':
    run_game()
