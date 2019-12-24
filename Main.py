from Helpers.Encounters import Enemy as EnemyEncounter
from Collections.Biomes import Biome
import random

playerBiome = Biome.Mountains
instruction_string = "Type 'next' for new encounter"

def StartBattle(enemy):
	print(enemy.art)
	print(f'''{enemy.name} - HP: {enemy.health_current}''')

def GetEncounter():
	StartBattle(EnemyEncounter.GetRandom(playerBiome))

def StartGameLoop():
	playerBiome = Biome.Mountains
	print(instruction_string)

	while True:
		command = input("> ").lower()
		if command == "next":
			GetEncounter()
			print(instruction_string)

StartGameLoop()