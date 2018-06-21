#! /usr/bin/env python


class ChessPlayer():
	def __init__(self,name,color):
		self.name = name
		self.color = color
		self.type = 'human'
		
	def GetName(self):
		return self.name
		
	def GetColor(self):
		return self.color
	
	def GetType(self):
		return self.type