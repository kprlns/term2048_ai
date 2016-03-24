import random
def get_ai_move(game):
	UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
	i=random.randint(0,100)
	""" Useful things:

		game.board - object of class Board

		game.board.cells - 2d array of cells, each cell is an int like 2, 4, 2048 etc

		game.board.getLine(y) - returns line number y
		game.board.getCol(x) - returns col number x
		game.board.getEmptyCells() - returns a list of x,y pairs for all empty cells




	Function has to return a swipe direction.

	Example - code returning a random direction:

	return random.choice(UP, DOWN, LEFT, RIGHT)

	"""

	if(i<80):
		return random.randint(2,3)
	elif i>97 and i<=100:
		return 4
