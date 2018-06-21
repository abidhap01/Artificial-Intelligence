#! /usr/bin/env python

from ChessRules import ChessRules
import random

class ChessAI():
	def __init__(self,name,color):
		self.name = name
		self.color = color
		self.type = 'AI'
		self.Rules = ChessRules()
		
	def GetName(self):
		return self.name
		
	def GetColor(self):
		return self.color
		
	def GetType(self):
		return self.type
		
	def GetMove(self,board,color):
		if color == "black":
			myColor = 'b'
			enemyColor = 'w'
		else:
			myColor = 'w'
			enemyColor = 'b'
		
		myPieces = []
		for row in range(8):
			for col in range(8):
				piece = board[row][col]
				if myColor in piece:
					if len(self.Rules.GetListOfValidMoves(board,color,(row,col))) > 0:
						myPieces.append((row,col))		
		
		fromTuple = myPieces[random.randint(0,len(myPieces)-1)]
		legalMoves = self.Rules.GetListOfValidMoves(board,color,fromTuple)
		toTuple = legalMoves[random.randint(0,len(legalMoves)-1)]
		
		moveTuple = (fromTuple,toTuple)
		return moveTuple