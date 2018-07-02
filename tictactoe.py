import random 

#Prints the board with its current values
def drawBoard():
	patterns = {1: "   |   |   ", 2: f" {cellValues[6]} | {cellValues[7]} | {cellValues[8]} ", 3: "-----------", 
				4: f" {cellValues[3]} | {cellValues[4]} | {cellValues[5]} ", 5: f" {cellValues[0]} | {cellValues[1]} | {cellValues[2]} "}
	board = [1,2,1,3,1,4,1,3,1,5,1]

	for x in board:
		print(patterns[x])

#Lets the players choose which characters they want to be
def setPlayers(players):
	while players[0] != "X" and players[0] != "O":
		players[0] = input("Player 1 do you wanna be X or O? \n").upper()
		if players[0] != "X" and players[0] != "O":
			print("That is not a valid option \n")
	
	if players[0] == "X":
		players[1] = "O"
	else:
		players[1] = "X"

	print(f"\nPlayer 1 is {players[0]}")
	print(f"Player 2 is {players[1]}")

#Places the player's character where they want it
def playerTurn(cellValues, currentPlayer):
	valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	cell = input(f"\nPlayer {currentPlayer + 1} where do you want to place your {players[currentPlayer]}?\n")
	
	while cell not in valid:
		cell = input("\nThat is not a valid answer, please choose a valid one (pick any number from 1-9)\n")
	else:
		cell = int(cell)

	
	while cellValues[cell - 1] != " ":
		print("\nThere is already a character in that location")
		cell = int(input(f"\nWhere do you want to place your {players[currentPlayer]}?\n"))
	else:
		cellValues[cell - 1] = players[currentPlayer]

def fullBoard(cellValues):
	for x in range(0,9):
		if cellValues[x] == " ":
			return False
	return True

#Checks at the end of the player turns if there is a winner
def checkWinner(cellValues,currentPlayer):
	for x in range(0,9):
		if cellValues[x] != " ":
			if x == 0 or x == 1 or x == 2:
				if cellValues[x] == cellValues[x + 3] and cellValues[x] == cellValues[x + 6]:
					print(f"\nPlayer {currentPlayer + 1} wins")
					return False
			if x == 0 or x == 3 or x == 6:
				if cellValues[x] == cellValues[x + 1] and cellValues[x] == cellValues[x + 2]:
					print(f"\nPlayer {currentPlayer + 1} wins")
					return False
			if x == 0:
				if cellValues[x] == cellValues[x + 4] and cellValues[x] == cellValues[x + 8]:
					print(f"\nPlayer {currentPlayer + 1} wins")
					return False
			if x == 2:
				if cellValues[x] == cellValues[x + 2] and cellValues[x] == cellValues[x + 4]:
					print(f"\nPlayer {currentPlayer + 1} wins")
					return False
	if fullBoard(cellValues):
		print("\nThe board is full")
		return False
	
	return True

cellValues = None
answer = None
players = ["", ""]
stillPlaying = True
playAgain = True

setPlayers(players)
currentPlayer = random.randrange(0,2)

while playAgain:
	cellValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
	answer = None
	print(f"\nPlayer {currentPlayer + 1} goes first\n")
	drawBoard()

	while stillPlaying:
		playerTurn(cellValues, currentPlayer)
		drawBoard()
		stillPlaying = checkWinner(cellValues,currentPlayer)
		if currentPlayer == 0:
			currentPlayer = 1
		else:
			currentPlayer = 0 

	while answer != "yes" and answer != "no":
		answer = input("\nDo  you want to play another round?\n").lower()
		if answer == "yes":
			stillPlaying = True
			playAgain = True
			break
		elif answer == "no":
			playAgain = False
			break
		
		print("\nThat is not a valid answer (yes/no)")