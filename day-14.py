import math

needed = {}

# needed = {
# 	'ABC' : {
# 		'mats' : {
# 			'BC' : 11,
# 			'ORE' : 20
# 		},
# 		'out' : 10
# 	}
# }
ore_mine = 1000000000000
fuel = 0

data_file = open('data-14.txt', 'r', encoding="utf8")
line = data_file.readline()
while line:
	parts = line.rstrip().split(' => ')
	result_part = parts[1].split(' ')
	src_part = parts[0].split(', ')
	needed[result_part[1]] = {
		'mats' : {},
		'out' : int(result_part[0])
	}
	
	for i,part in enumerate(src_part):
		item = part.split(' ')
		needed[result_part[1]]['mats'][item[1]] = int(item[0])
	line = data_file.readline()

leftovers = {}

def getMatsFor(material, quantity):
	global leftovers
	if quantity == 0:
		return 0
	source = needed[material]
	mult = 1
	ores = 0
	mult = math.ceil(quantity / source['out'])
	# print('produce ' + str(mult * source['out']) + ' of ' + material)
	for _, key in enumerate(source['mats']):
		if key == 'ORE':
			ores += mult * source['mats'][key]
		else:
			todo = mult * source['mats'][key]
			if key in leftovers:
				to_take = min(todo, leftovers[key])
				todo -= to_take
				leftovers[key] -= to_take
			ores += getMatsFor(key, todo)
	if material != 'ORE':
		if not material in leftovers:
			leftovers[material] = 0
		leftovers[material] += mult * source['out'] - quantity
	return ores


ore_round = 0
fuel_to_make = 2**0

one_fuel = getMatsFor('FUEL', 1)
leftovers = {}

fuel = math.floor(ore_mine / one_fuel)
ore_mine -= getMatsFor('FUEL', fuel) 

d_fuel = math.floor(ore_mine / one_fuel)

while d_fuel > 1000:
	ore_mine -= getMatsFor('FUEL', d_fuel)
	fuel += d_fuel
	d_fuel = math.floor(ore_mine / one_fuel)

while ore_mine > ore_round:
	ore_round = getMatsFor('FUEL', fuel_to_make)
	fuel += fuel_to_make
	ore_mine -= ore_round
	if fuel % 1000 == 0:
		print(fuel)

# 7659731 - too low

# while fuel_to_make > 0:
# 	while ore_mine > ore_round:
# 		ore_round = getMatsFor('FUEL', fuel_to_make)
# 		fuel += fuel_to_make
# 		ore_mine -= ore_round
# 		# if fuel % 1000 == 0:
# 		print(fuel)
# 		print('ore left: ' + str(ore_mine))
# 	fuel_to_make =  int(fuel_to_make / 2)

# fuel -= 1
print(fuel)
