def drawBoard(cell):
	cellValues[cell - 1] = "X"
	
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
		players[0] = input("Player 1 do you wanna be X or O?").upper()
		if players[0] != "X" and players[0] != "O":
			print("That is not a valid option")
	
	if players[0] == "X":
		players[1] = "O"
	else:
		players[1] = "X"

	print(f"Player 1 is {players[0]}")
	print(f"Player 2 is {players[1]}")


cellValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
players = ["", ""]

setPlayers(players)
cell = int(input())
drawBoard(cell)
