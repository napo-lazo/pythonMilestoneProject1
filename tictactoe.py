import random 

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


cellValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
players = ["", ""]
stillPlaying = True

setPlayers(players)
currentPlayer = random.randrange(0,2)
print(f"\nPlayer {currentPlayer + 1} goes first\n")
drawBoard()

while stillPlaying:
	cell = int(input(f"\nPlayer {currentPlayer + 1} where do you want to place your {players[currentPlayer]}?\n"))
	cellValues[cell - 1] = players[currentPlayer]
	drawBoard()
	if currentPlayer == 0:
		currentPlayer = 1
	else:
		currentPlayer = 0 