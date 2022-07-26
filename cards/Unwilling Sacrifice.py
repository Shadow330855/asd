#!/user/bin/env python

from cardList import addCard
import mechanics
import random

#Simple variables
NAME = "Unwilling Sacrifice"
COST = 4
RARITY = 'U'
DESC = "Choose and sacrifice a friendly Node. Destroy a random enemy Node."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.sacNode(ply, enemy, target)
	if len(enemy.nodes) > 0:
		target = random.randint(0,len(enemy.nodes)-1)
		await mechanics.sacNode(enemy, ply, target)
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

