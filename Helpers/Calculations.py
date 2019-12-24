class Stats:

	# scale a value using base_value * growth_percent * level
	# eg. 20 hp, 25 percent
	# level 1 = 20hp
	# level 2 = 25hp
	# level 10 = 65hp
	def ScaleByLevel(base_value, growth_percent, level):
		if level <= 1:
			return base_value
		else:
			levelup_count = level - 1
			per_level_increase = base_value * growth_percent / 100
			return per_level_increase * levelup_count + base_value