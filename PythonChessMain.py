#! /usr/bin/env python
"""
 Project: Python Chess
 File name: PythonChessMain.py
 Description:  Chess for player vs. player, player vs. AI, or AI vs. AI.
    Uses Tkinter to get initial game parameters.
	Uses Pygame to draw the board and pieces and to get user mouse clicks.
 Copyright (C) 2009 Steve Osborne, srosborne (at) gmail.com
 
 *******
 This program is free software; you can redistribute it and/or modify 
 it under the terms of the GNU General Public License as published by 
 the Free Software Foundation; either version 2 of the License, or 
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful, but 
 WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
 or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
 for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

 *******
 Version history:

 v 0.4 - 14 April 2009.  Added better chess piece graphics from Wikimedia
   Commons.  Added a Tkinter dialog box (ChessGameParams.py) for getting
   the game setup parameters.  Converted to standard chess notation for 
   move reporting and added row/col labels around the board.
 
 v 0.3 - 06 April 2009.  Added pygame graphical interface.  Includes
   addition of ScrollingTextBox class.
   
 v 0.2 - 04 April 2009.  Broke up the program into classes that will
   hopefully facilitate easily incorporating graphics or AI play.
 
 v 0.1 - 01 April 2009.  Initial release.  Draws the board, accepts
   move commands from each player, checks for legal piece movement.
   Appropriately declares player in check or checkmate.


 To do:
   Add in better AI
 
"""

from ChessBoard import ChessBoard
from ChessAI import ChessAI
from ChessPlayer import ChessPlayer
from ChessGUI_text import ChessGUI_text
from ChessGUI_pygame import ChessGUI_pygame
from ChessRules import ChessRules
from ChessGameParams import TkinterGameSetupParams

import sys

class PythonChessMain:
	def __init__(self,options):
		if 'd' in options:
			self.Board = ChessBoard(2)
			self.debugMode = True
		else:
			self.Board = ChessBoard(0)#0 for normal board setup; see ChessBoard class for other options (for testing purposes)
			self.debugMode = False

		self.Rules = ChessRules()
		
	def SetUp(self,options):
		#gameSetupParams: Player 1 and 2 Name, Color, Human/AI level
		if self.debugMode:
			player1Name = 'Steve'
			player1Type = 'human'
			player1Color = 'white'
			player2Name = 'Bob'
			player2Type = 'AI'
			player2Color = 'black'		
		else:
			GameParams = TkinterGameSetupParams()
			(player1Name, player1Color, player1Type, player2Name, player2Color, player2Type) = GameParams.GetGameSetupParams()

		self.player = [0,0]
		if player1Type == 'human':
			self.player[0] = ChessPlayer(player1Name,player1Color)
		else:
			self.player[0] = ChessAI(player1Name,player1Color)
			
		if player2Type == 'human':
			self.player[1] = ChessPlayer(player2Name,player2Color)
		else:
			self.player[1] = ChessAI(player2Name,player2Color)
			
		#create the gui object - didn't do earlier because pygame conflicts with any gui manager (Tkinter, WxPython...)
		if 't' in options:
			self.guitype = 'text'
			self.Gui = ChessGUI_text()
		else:
			self.guitype = 'pygame'
			if 'o' in options:
				self.Gui = ChessGUI_pygame(0)
			else:
				self.Gui = ChessGUI_pygame(1)
			
	def MainLoop(self):
		currentPlayerIndex = 0
		turnCount = 0
		while not self.Rules.IsCheckmate(self.Board.GetState(),self.player[currentPlayerIndex].color):
			board = self.Board.GetState()
			currentColor = self.player[currentPlayerIndex].GetColor()
			#hardcoded so that player 1 is always white
			if currentColor == 'white':
				turnCount = turnCount + 1
			self.Gui.Draw(board)
			self.Gui.PrintMessage("")
			self.Gui.PrintMessage("-----------TURN "+str(turnCount)+" - "+ self.player[currentPlayerIndex].GetName() +" ("+currentColor+")-----------")
			if self.Rules.IsInCheck(board,currentColor):
				self.Gui.PrintMessage("Warning..."+self.player[currentPlayerIndex].GetName()+" ("+self.player[currentPlayerIndex].GetColor()+") is in check!")
			
			if self.player[currentPlayerIndex].GetType() == 'AI':
				moveTuple = self.player[currentPlayerIndex].GetMove(self.Board.GetState(), currentColor) 
			else:
				moveTuple = self.Gui.GetPlayerInput(board,currentColor)
			moveReport = self.Board.MovePiece(moveTuple) #moveReport = string like "White Bishop moves from A1 to C3" (+) "and captures ___!"
			self.Gui.PrintMessage(moveReport)
			currentPlayerIndex = (currentPlayerIndex+1)%2 #this will cause the currentPlayerIndex to toggle between 1 and 0
		
		self.Gui.PrintMessage("CHECKMATE!")
		winnerIndex = (currentPlayerIndex+1)%2
		self.Gui.PrintMessage(self.player[winnerIndex].GetName()+" ("+self.player[winnerIndex].GetColor()+") won the game!")
		self.Gui.Draw(board) #draw board a final time to show the end game
		c = raw_input("Game finished...press any key to quit.")#pause at the end
		if self.guitype == 'pygame':
			pygame.quit()
		
options = ""
if 'debug' in sys.argv:
	options = options + 'd'
#text gui:
if 'text' in sys.argv:
	options = options + 't'
#old graphics:
if 'old' in sys.argv:
	options = options + 'o'
game = PythonChessMain(options)#'d' for debug, 't' for text-graphics
game.SetUp(options)
game.MainLoop()


	