import sys
from GameBoard import *

def getSudokuGrid(fileName):
	sudokuFile = open(fileName, 'r')
	gridList = []
	sudokuGrid = ""

	# reads in each line of the sudoku file
	for line in sudokuFile:
		# if the line is part of the sudoku grid, save it in sudokuGrid
		if line.isdigit():
			sudokuGrid += line
		# ignores \n at the end of a line.
		elif line[:-1].isdigit():
			sudokuGrid += line[:-1]
		# when a grid is complete, add it to the gridList
		if len(sudokuGrid) == 81:
			gridList.append(GameBoard(list(sudokuGrid)))
			sudokuGrid = ""

	return gridList


# MAIN METHOD
def main(fileName):
	gridList = getSudokuGrid(fileName)
	gridList[2].printGrid()
	gridList[2].solve()
	gridList[2].printGrid()

if __name__ == '__main__':
	main(sys.argv[1])