def init_game():
	def print_board(board):
		line_one = print(f'{board['1']} | {board['2']} | {board['3']}' )
		line_two = print(f'{board['4']} | {board['5']} | {board['6']}' )
		line_three = print(f'{board['7']} | {board['8']} | {board['9']}' )
	
	def get_user_input(player, board):
		is_valid = False
		marker = "X" if player == "player_one" else "O"
		player_name = "Player One" if player == "player_one" else "Player Two"
	
		while(not is_valid):
			answer = input(f"Hello {player_name}. Choose the location of your next move by entering a number between 1 to 9: ")
			key = 1
			if(not answer.isdigit()):
				print("Your input was not a number")
			elif(not 1 <= int(answer) <= 9 ):
				print("Your input was not a number between 1 to 9")
			elif(not type(board[answer]) == int):
				print("That spot has already been taken")
			else:
				is_valid = True
	
		board[answer] = marker
		print_board(board)
	
	def check_win_condition(game_over, board):
		winning_combinations = (('1','2','3'),('4','5','6'),('7','8','9'),('1','4','7'),('2','5','8'),('3','6','9'),('1','5','9'),('3','5','7'))
		for a,b,c in winning_combinations:
			# if((board[a] == board[b] == board[c]) and type(board[a]) == str):
			if(board[a] == board[b] == board[c]):
				if(board[a] == "X"):
					print("Player One has won!")
					return True
				else:
					print("Player Two has won!")		
					return True
		if(all(isinstance(value, str) for value in board.values())):
			print("Game is over with no winners!")
			return True
		return False			
	
	def switch_players(player):
		if(player == "player_one"):
			return "player_two"
		else:
			return "player_one"

	board = {'1': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7':7, '8':8,'9':9}
	print("Welcome players! Shown below is the board")
	print_board(board)
	game_over = False
	player = "player_one"
	while(not game_over):
		get_user_input(player, board)
		game_over = check_win_condition(game_over, board) #scope of game_over doesn't carry over because game_over gets redefined in the scope of a function
		player = switch_players(player)
	is_replay = input("Game Over! Enter 'Y' to play again. \n")
	if(is_replay == "Y"):
		init_game()

init_game()
