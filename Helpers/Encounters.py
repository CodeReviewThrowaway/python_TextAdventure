import random
from Collections.Biomes import Biome

class Enemy:
	def GetRandom(biome):
		pool = []
		if biome == Biome.Forest:
			pool = EnemyPool.forest
		elif biome == Biome.Mountains:
			pool = EnemyPool.mountains
		else:
			TypeError("Biome is null")

		return  random.choice(pool)()



from Collections.Enemies import Factory as F

class EnemyPool:
	forest = [F.GetGoblin]
	mountains = [F.GetDragon, F.GetFeralGoblin]
