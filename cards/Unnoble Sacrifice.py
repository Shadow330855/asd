#!/user/bin/env python

from cardList import addCard
import mechanics, math

#Simple variables
NAME = "Unnoble Sacrifice"
COST = 13
RARITY = 'R'
DESC = "Lose half your lifeforce, rounded up. Your opponent burns that many cards."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	lifeLost = math.ceil( ply.lifeforce / 2 )
	await mechanics.damage( ply, lifeLost )
	await enemy.burn( lifeLost )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

