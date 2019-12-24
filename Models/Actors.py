from abc import ABC, abstractmethod
# Abstract Base Classes cannot be instantiated and must be extended in the form of a child class.
# This allows us to set a basic template that can be shared between different types of actors but cannot be instantiated as it's own object.

# The abstract base class for an actor, this is the initial template all actors will build from
class Actor(ABC):
	@abstractmethod
	def __init__(self, name, art):
		self.name = name
		self.art = art

# Abstract class for actors who can engage in combat.
# This is an extension of the Actor class. 
class CombatActor(Actor, ABC):
	@abstractmethod
	def __init__(self, name, art, attack, health, strength):
		Actor.__init__(self, name, art)
		self.attack = attack
		self.health = health
		self.strength = strength
		self.health_current = health

# This class extends the CombatActor class
# This class is not abstract and can be instantiased
class Monster(CombatActor):
	def __init__(self, name, art, attack, health, strength, exp_drop, gold_drop):
		CombatActor.__init__(self, name, art, attack, health, strength)
		self.gold_drop = gold_drop
		self.exp_drop = exp_drop

from Helpers.Calculations import Stats as CalcStats
# This class extends the Monster class
# This class is not abstract and can be instantiased
class MonsterScaled(Monster):
	def __init__(self, name, art, level, attack, attack_growth, health, health_growth, strength, strength_growth, exp_drop, exp_growth, gold_drop, gold_growth):
		scaled_attack = CalcStats.ScaleByLevel(attack, attack_growth, level)
		scaled_health = CalcStats.ScaleByLevel(health, health_growth, level)
		scaled_strength = CalcStats.ScaleByLevel(strength, strength_growth, level)
		scaled_exp_drop = CalcStats.ScaleByLevel(exp_drop, exp_growth, level)
		scaled_gold_drop = CalcStats.ScaleByLevel(gold_drop, gold_growth, level)
		Monster.__init__(self, name, art, scaled_attack, scaled_health, scaled_strength, scaled_exp_drop, scaled_gold_drop)

	

# This class extends the CombatActor class
# This class is not abstract and can be instantiased
class Player(CombatActor):
	def __init__(self, name, art, attack, health, strength, gold):
		CombatActor.__init__(self, name, art, attack, health, strength)
		self.exp = 0
		self.gold = gold
		
		# Weapons class & custom weapons objects should be created.
		self.weapon = "undefined"
