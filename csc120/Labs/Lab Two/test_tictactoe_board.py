"""Testing the tictactoe_board module.

Authors: Kristina Striegnitz
Version: fall 2023
"""

import tictactoe_board as ttt_board

def test_suite():
    '''
    performs a variety of tests on typical tic tac toe game outcomes
    '''
    confirm_result(['XXX', 'OOX', 'OOX'],'X')
    confirm_result(['OXO', 'OXX', 'OOX'],'O')
    confirm_result(['OOO', 'OXX', 'XOX'],'O')
    confirm_result(['OOX', 'OXX', 'XOX'],'X')
    confirm_result(['OXO','XOX','XXO'],'O')    
    confirm_result(['OOX','OXO','XOO'],'X')
    

def confirm_result(board, winner):
    ttt_board.show(board)
    board = ttt_board.create(board)
    programs_winner = ttt_board.get_winner(board)
    if programs_winner == winner:
        print("PASS")
    else:
        print('FAIL')



 


if __name__ == "__main__":
    test_suite(); 


