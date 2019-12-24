import random
from Models import Actors
from Collections.Art import Library as ArtLibrary

class Factory:

	def GetGoblin():
		return Actors.Monster("Goblin", ArtLibrary.goblin, 5, 10, 5, 15, 30)

	def GetFeralGoblin():
		level = random.randint(1,10)
		return Actors.MonsterScaled("Goblin", ArtLibrary.goblin, level, 5, 25, 10, 50, 5, 25, 15, 50, 30, 33)

	def GetDragon():
		return Actors.Monster("Dragon", ArtLibrary.dragon, 20, 100, 40, 1000, 500)
	


