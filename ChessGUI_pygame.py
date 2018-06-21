#! /usr/bin/env python
#The chess tile graphics were taken from Wikimedia Commons, http://commons.wikimedia.org/wiki/File:Chess_tile_pd.png
import pygame
import os
from pygame.locals import *
from ChessRules import ChessRules
from ScrollingTextBox import ScrollingTextBox
from ChessBoard import ChessBoard

class ChessGUI_pygame:
	def __init__(self,graphicStyle):
		os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
		self.Rules = ChessRules()
		pygame.init()
		pygame.display.init()
		self.screen = pygame.display.set_mode((850,500))
		self.boardStart_x = 50
		self.boardStart_y = 50
		pygame.display.set_caption('Python Chess')

		self.textBox = ScrollingTextBox(self.screen,525,850,50,450)
		self.LoadImages(graphicStyle)
		#pygame.font.init() - should be already called by pygame.init()
		self.fontDefault = pygame.font.Font( None, 20 )
		

	def LoadImages(self,graphicStyle):
		if graphicStyle == 0:
			self.square_size = 50 #all images must be images 50 x 50 pixels
			self.white_square = pygame.image.load("white_square.png").convert()
			self.brown_square = pygame.image.load("brown_square.png")
			self.cyan_square = pygame.image.load("cyan_square.png")
			self.black_pawn = pygame.image.load("blackPawn.png")
			self.black_rook = pygame.image.load("blackRook.png")
			self.black_knight = pygame.image.load("blackKnight.png")
			self.black_bishop = pygame.image.load("blackBishop.png")
			self.black_king = pygame.image.load("blackKing.png")
			self.black_queen = pygame.image.load("blackQueen.png")
			self.white_pawn = pygame.image.load("whitePawn.png")
			self.white_rook = pygame.image.load("whiteRook.png")
			self.white_knight = pygame.image.load("whiteKnight.png")
			self.white_bishop = pygame.image.load("whiteBishop.png")
			self.white_king = pygame.image.load("whiteKing.png")
			self.white_queen = pygame.image.load("whiteQueen.png")
		elif graphicStyle == 1:
			self.square_size = 50
			self.white_square = pygame.image.load("white_square.png").convert()
			self.brown_square = pygame.image.load("brown_square.png").convert()
			self.cyan_square = pygame.image.load("cyan_square.png").convert()
			
			self.black_pawn = pygame.image.load("Chess_tile_pd.png").convert()
			self.black_pawn = pygame.transform.scale(self.black_pawn, (self.square_size,self.square_size))
			self.black_rook = pygame.image.load("Chess_tile_rd.png").convert()
			self.black_rook = pygame.transform.scale(self.black_rook, (self.square_size,self.square_size))
			self.black_knight = pygame.image.load("Chess_tile_nd.png").convert()
			self.black_knight = pygame.transform.scale(self.black_knight, (self.square_size,self.square_size))
			self.black_bishop = pygame.image.load("Chess_tile_bd.png").convert()
			self.black_bishop = pygame.transform.scale(self.black_bishop, (self.square_size,self.square_size))
			self.black_king = pygame.image.load("Chess_tile_kd.png").convert()
			self.black_king = pygame.transform.scale(self.black_king, (self.square_size,self.square_size))
			self.black_queen = pygame.image.load("Chess_tile_qd.png").convert()
			self.black_queen = pygame.transform.scale(self.black_queen, (self.square_size,self.square_size))

			self.white_pawn = pygame.image.load("Chess_tile_pl.png").convert()
			self.white_pawn = pygame.transform.scale(self.white_pawn, (self.square_size,self.square_size))
			self.white_rook = pygame.image.load("Chess_tile_rl.png").convert()
			self.white_rook = pygame.transform.scale(self.white_rook, (self.square_size,self.square_size))
			self.white_knight = pygame.image.load("Chess_tile_nl.png").convert()
			self.white_knight = pygame.transform.scale(self.white_knight, (self.square_size,self.square_size))
			self.white_bishop = pygame.image.load("Chess_tile_bl.png").convert()
			self.white_bishop = pygame.transform.scale(self.white_bishop, (self.square_size,self.square_size))
			self.white_king = pygame.image.load("Chess_tile_kl.png").convert()
			self.white_king = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))
			self.white_queen = pygame.image.load("Chess_tile_ql.png").convert()
			self.white_queen = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))


	def PrintMessage(self,message):
		#prints a string to the area to the right of the board
		self.textBox.Add(message)
		
	def ConvertToScreenCoords(self,chessSquareTuple):
		#converts a (row,col) chessSquare into the pixel location of the upper-left corner of the square
		(row,col) = chessSquareTuple
		screenX = self.boardStart_x + col*self.square_size
		screenY = self.boardStart_y + row*self.square_size
		return (screenX,screenY)
		
	def ConvertToChessCoords(self,screenPositionTuple):
		#converts a screen pixel location (X,Y) into a chessSquare tuple (row,col)
		#x is horizontal, y is vertical
		#(x=0,y=0) is upper-left corner of the screen
		(X,Y) = screenPositionTuple
		row = (Y-self.boardStart_y) / self.square_size
		col = (X-self.boardStart_x) / self.square_size
		return (row,col)
		
		
	def Draw(self,board,highlightSquares=[]):
		self.textBox.Draw()
		boardSize = len(board) #board should be square.  boardSize should be always 8 for chess, but I dislike "magic numbers" :)

		#draw blank board
		current_square = 0
		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				if current_square:
					self.screen.blit(self.brown_square,(screenX,screenY))
					current_square = (current_square+1)%2
				else:
					self.screen.blit(self.white_square,(screenX,screenY))
					current_square = (current_square+1)%2

			current_square = (current_square+1)%2

		#draw row/column labels around the edge of the board
		chessboard_obj = ChessBoard(0)#need a dummy object to access some of ChessBoard's methods....
		color = (255,255,255)#white
		antialias = 0
		
		#top and bottom - display cols
		for c in range(boardSize):
			for r in [-1,boardSize]:
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				screenX = screenX + self.square_size/2
				screenY = screenY + self.square_size/2
				notation = chessboard_obj.ConvertToAlgebraicNotation_col(c)
				renderedLine = self.fontDefault.render(notation,antialias,color)
				self.screen.blit(renderedLine,(screenX,screenY))
		
		#left and right - display rows
		for r in range(boardSize):
			for c in [-1,boardSize]:
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				screenX = screenX + self.square_size/2
				screenY = screenY + self.square_size/2
				notation = chessboard_obj.ConvertToAlgebraicNotation_row(r)
				renderedLine = self.fontDefault.render(notation,antialias,color)
				self.screen.blit(renderedLine,(screenX,screenY))
				
		#highlight squares if specified
		for square in highlightSquares:
			(screenX,screenY) = self.ConvertToScreenCoords(square)
			self.screen.blit(self.cyan_square,(screenX,screenY))
		
		#draw pieces
		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				if board[r][c] == 'bP':
					self.screen.blit(self.black_pawn,(screenX,screenY))
				if board[r][c] == 'bR':
					self.screen.blit(self.black_rook,(screenX,screenY))
				if board[r][c] == 'bT':
					self.screen.blit(self.black_knight,(screenX,screenY))
				if board[r][c] == 'bB':
					self.screen.blit(self.black_bishop,(screenX,screenY))
				if board[r][c] == 'bQ':
					self.screen.blit(self.black_queen,(screenX,screenY))
				if board[r][c] == 'bK':
					self.screen.blit(self.black_king,(screenX,screenY))
				if board[r][c] == 'wP':
					self.screen.blit(self.white_pawn,(screenX,screenY))
				if board[r][c] == 'wR':
					self.screen.blit(self.white_rook,(screenX,screenY))
				if board[r][c] == 'wT':
					self.screen.blit(self.white_knight,(screenX,screenY))
				if board[r][c] == 'wB':
					self.screen.blit(self.white_bishop,(screenX,screenY))
				if board[r][c] == 'wQ':
					self.screen.blit(self.white_queen,(screenX,screenY))
				if board[r][c] == 'wK':
					self.screen.blit(self.white_king,(screenX,screenY))
			
		pygame.display.flip()

	def GetPlayerInput(self,board,currentColor):
		#returns ((from_row,from_col),(to_row,to_col))
		fromSquareChosen = 0
		toSquareChosen = 0
		while not fromSquareChosen or not toSquareChosen:
			squareClicked = []
			for e in pygame.event.get():
				if e.type is KEYDOWN:
					if e.key is K_ESCAPE:
						fromSquareChosen = 0
						fromTuple = []
				if e.type is MOUSEBUTTONDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					squareClicked = self.ConvertToChessCoords((mouseX,mouseY))
					if squareClicked[0]<0 or squareClicked[0]>7 or squareClicked[1]<0 or squareClicked[1]>7:
						squareClicked = [] #not a valid chess square
				if e.type is QUIT: #the "x" kill button
					pygame.quit()
					exit()
					
			if not fromSquareChosen and not toSquareChosen:
				self.Draw(board)
				if squareClicked != []:
					(r,c) = squareClicked
					if currentColor == 'black' and 'b' in board[r][c]:
						if len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
					elif currentColor == 'white' and 'w' in board[r][c]:
						if len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
						
			elif fromSquareChosen and not toSquareChosen:
				possibleDestinations = self.Rules.GetListOfValidMoves(board,currentColor,fromTuple)
				self.Draw(board,possibleDestinations)
				if squareClicked != []:
					(r,c) = squareClicked
					if squareClicked in possibleDestinations:
						toSquareChosen = 1
						toTuple = squareClicked
					elif currentColor == 'black' and 'b' in board[r][c]:
						if squareClicked == fromTuple:
							fromSquareChosen = 0
						elif len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
						else:
							fromSquareChosen = 0 #piece is of own color, but no possible moves
					elif currentColor == 'white' and 'w' in board[r][c]:
						if squareClicked == fromTuple:
							fromSquareChosen = 0
						elif len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
						else:
							fromSquareChosen = 0
					else: #blank square or opposite color piece not in possible destinations clicked
						fromSquareChosen = 0

		return (fromTuple,toTuple)

	def GetClickedSquare(self,mouseX,mouseY):
		#test function
		print "User clicked screen position x =",mouseX,"y =",mouseY
		(row,col) = self.ConvertToChessCoords((mouseX,mouseY))
		if col < 8 and col >= 0 and row < 8 and row >= 0:
			print "  Chess board units row =",row,"col =",col

	def TestRoutine(self):
		#test function
		while 1:
			for e in pygame.event.get():
				if e.type is QUIT:
					return
				if e.type is KEYDOWN:
					if e.key is K_ESCAPE:
						pygame.quit()
						return
				if e.type is MOUSEBUTTONDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					#x is horizontal, y is vertical
					#(x=0,y=0) is upper-left corner of the screen
					self.GetClickedSquare(mouseX,mouseY)


if __name__ == "__main__":
	#try out some development / testing stuff if this file is run directly
	testBoard = [['bR','bT','bB','bQ','bK','bB','bT','bR'],\
				 ['bP','bP','bP','bP','bP','bP','bP','bP'],\
				 ['e','e','e','e','e','e','e','e'],\
				 ['e','e','e','e','e','e','e','e'],\
				 ['e','e','e','e','e','e','e','e'],\
				 ['e','e','e','e','e','e','e','e'],\
				 ['wP','wP','wP','wP','wP','wP','wP','wP'],\
				 ['wR','wT','wB','wQ','wK','wB','wT','wR']]
				 
	validSquares = [(5,2),(1,1),(1,5),(7,6)]

	game = ChessGUI_pygame()
	game.Draw(testBoard,validSquares)
	game.TestRoutine()
	
