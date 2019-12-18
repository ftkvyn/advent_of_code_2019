import math

sum = 0 

data_file = open('data-01.txt', 'r', encoding="utf8")
line = data_file.readline()
while line:
	totalFuel = 0
	fuel = 0
	mass = int(line)
	fuel = math.floor(mass / 3) - 2	
	newFuel =  math.floor(fuel / 3) - 2
	if newFuel < 0:
		newFuel = 0
	totalFuel = fuel
	while newFuel > 0:
		totalFuel += newFuel
		newFuel =  math.floor(newFuel / 3) - 2
	sum += totalFuel
	print(totalFuel)
	line = data_file.readline()
	print('--------------------')

print(sum)