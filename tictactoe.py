import sys

winner = None
player1 = None
player2 = None
currentPlayer = None
test_board = [' ']*10
my_dict = {'Player 1':'X', 'Player 2':'O'}

# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def player_input():
	player_input = input("Player 1, Enter X or O:")
	
	if(player_input == 'X' or player_input == 'O'):
		if(player_input == 'X'):
			my_dict['Player 1'] = 'X'
			my_dict['Player 2'] = 'O'
		else:
			my_dict['Player 1'] = 'O'
			my_dict['Player 2'] = 'X'

	return (my_dict['Player 1'], my_dict['Player 2'])

def display_board(board):
	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])	

def play_game():
	global player1
	global player2
	global currentPlayer
	global test_board

	#alternate players
	if(currentPlayer == None):
		currentPlayer = 'Player 1'
	elif(currentPlayer == 'Player 1'):
		currentPlayer = 'Player 2'
	else:
		currentPlayer = 'Player 1'

	#play turn
	position = int(input(currentPlayer + ", Enter position 1 to 9:"))
	if(position <=9 and position >=1):
		print(get_key(my_dict[currentPlayer]) + " selected " + ascii(position))
		test_board[position] = my_dict[currentPlayer]  

def print_winner(player=currentPlayer):
	global currentPlayer
	global winner
	winner = currentPlayer
	print("Winner is " +  winner)

def check_winner(board, player):
	global test_board
	global currentPlayer
	#check horizontal 
	if(board[1]==player and board[2]==player and board[3]==player):
		print_winner()
	if(board[4]==player and board[5]==player and board[6]==player):
		print_winner()
	if(board[7]==player and board[8]==player and board[9]==player):
		print_winner()
	#check vertical
	if(board[1]==player and board[4]==player and board[7]==player):
		print_winner()
	if(board[2]==player and board[5]==player and board[8]==player):
		print_winner()
	if(board[3]==player and board[6]==player and board[9]==player):
		print_winner()
	#check diagonal
	if(board[1]==player and board[5]==player and board[9]==player):
		print_winner()
	if(board[3]==player and board[5]==player and board[7]==player):
		print_winner()

def main():
	global player1
	global player2
	global winner

	print("Zahid's Tic Tac Toe Game")
    
	while(winner == None):
		if(player1 == None or player2 == None):
			(player1, player2) = player_input()
			print("Player 1 is " + player1)
			print("Player 2 is " + player2)

		play_game()
		display_board(test_board)
		check_winner(test_board, player1)
		check_winner(test_board, player2)
	
	sys.exit()

if __name__ == "__main__":
    main()