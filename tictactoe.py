import random 

#Prints the board with its current values
def drawBoard():
	print("   |   |   ")
	print(f" {cellValues[6]} | {cellValues[7]} | {cellValues[8]} ")
	print("   |   |   ")
	print("-----------")
	print("   |   |   ")
	print(f" {cellValues[3]} | {cellValues[4]} | {cellValues[5]} ")
	print("   |   |   ")
	print("-----------")
	print("   |   |   ")
	print(f" {cellValues[0]} | {cellValues[1]} | {cellValues[2]} ")
	print("   |   |   ")

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
	cell = int(input(f"\nPlayer {currentPlayer + 1} where do you want to place your {players[currentPlayer]}?\n"))
	while cellValues[cell - 1] != " ":
		print("\nThere is already a character in that location")
		cell = int(input(f"\nWhere do you want to place your {players[currentPlayer]}?\n"))
	else:
		cellValues[cell - 1] = players[currentPlayer]

#Checks at the end of the player turns if there is a winner
def checkWinner(cellValues):
	for x in range(0,9):
		if cellValues[x] != " ":
			if x == 0 or x == 1 or x == 2:
				if cellValues[x] == cellValues[x + 3] and cellValues[x] == cellValues[x + 6]:
					return False
			if x == 0 or x == 3 or x == 6:
				if cellValues[x] == cellValues[x + 1] and cellValues[x] == cellValues[x + 2]:
					return False
			if x == 0 or x == 2:
				if cellValues[x] == cellValues[x + 4] and cellValues[x] == cellValues[x + 8]:
					return False
	return True


cellValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
players = ["", ""]
stillPlaying = True

setPlayers(players)
currentPlayer = random.randrange(0,2)
print(f"\nPlayer {currentPlayer + 1} goes first\n")
drawBoard()

while stillPlaying:
	playerTurn(cellValues, currentPlayer)
	drawBoard()
	stillPlaying = checkWinner(cellValues)
	if currentPlayer == 0:
		currentPlayer = 1
	else:
		currentPlayer = 0 