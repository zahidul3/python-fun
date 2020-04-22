import sys
import random

winner = None
player1_marker = None
player2_marker = None
currentPlayer = None
the_board = ['#','1','2','3','4','5','6','7','8','9']
my_dict = {'Player 1':'X', 'Player 2':'O'}

# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def player_input():
	global my_dict
	player_input = input("Player 1, Enter X or O:")
	
	if(player_input.lower() == 'x' or player_input.lower() == 'o'):
		if(player_input.lower() == 'x'):
			my_dict['Player 1'] = 'X'
			my_dict['Player 2'] = 'O'
		else:
			my_dict['Player 1'] = 'O'
			my_dict['Player 2'] = 'X'

	return (my_dict['Player 1'], my_dict['Player 2'])

def space_valid(board, position):
	if position not in range(1,10,1):
		print(f"Invalid input:{position}, enter correct number")
		return False
	elif (board[position] != ' '):
		print("Invalid input, enter another number")
		return False
	else:
		return True

def display_board(board):
	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])	

def choose_first():
	flip = random.randint(0,1)
	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def player_choice(board):
	position = 0
	while True:
		position = int(input(currentPlayer + ", Enter position 1 to 9:"))
		if (space_valid(the_board,position)):
			break
	
	return position

def play_game():
	global player1_marker
	global player2_marker
	global currentPlayer
	global the_board
	
	position = 0
	
	#alternate players
	if(currentPlayer == None):
		currentPlayer = choose_first()
	elif(currentPlayer == 'Player 1'):
		currentPlayer = 'Player 2'
	else:
		currentPlayer = 'Player 1'

	#play turn
	position = player_choice(the_board)

	print(get_key(my_dict[currentPlayer]) + " selected " + ascii(position))
	the_board[position] = my_dict[currentPlayer]  

def print_winner(player=currentPlayer):
	global currentPlayer
	global winner
	winner = currentPlayer
	print("Winner is " +  winner)

def check_winner(board, player):
	global the_board
	global currentPlayer
	#check horizontal 
	if((board[1]==player and board[2]==player and board[3]==player) or
	(board[4]==player and board[5]==player and board[6]==player) or
	(board[7]==player and board[8]==player and board[9]==player) or
	#check vertical
	(board[1]==player and board[4]==player and board[7]==player) or
	(board[2]==player and board[5]==player and board[8]==player) or
	(board[3]==player and board[6]==player and board[9]==player) or
	#check diagonal
	(board[1]==player and board[5]==player and board[9]==player) or
	(board[3]==player and board[5]==player and board[7]==player)):
		print_winner()
		return winner
	else:
		return False

def check_board_full(board):
	for i in range(1,10,1):
		if board[i] == ' ':
			return False
	return True

def reset_game():
	global the_board
	global winner
	the_board = [' ']*10
	winner = None

def main():
	global the_board
	global player1_marker
	global player2_marker
	global winner
	replay = True
	board_full = False
    
	print("Zahid's Tic Tac Toe Game")
	display_board(the_board)
	reset_game()

	while(replay == True):
		if(player1_marker == None or player2_marker == None):
			(player1_marker, player2_marker) = player_input()
			print("Player 1 is " + player1_marker)
			print("Player 2 is " + player2_marker)

		play_game()
		display_board(the_board)
		check_winner(the_board, player1_marker)
		check_winner(the_board, player2_marker)
		board_full = check_board_full(the_board)
		if(board_full == True):
			print("Cat wins!")
			replay = False
		if(winner == get_key('X') or winner == get_key('O')):
			replay = False

	sys.exit()

if __name__ == "__main__":
    main()