from copy import copy, deepcopy
# y = deepcopy(x)

# positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# positions = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
positions = [[13, 9, 5], [8, 14, -2], [-5, 4, 11], [2, -6, 1]]

velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

statesX = []
statesY = []
statesZ = []

found = [0,0,0]

def strToNum(val):
	res = 0
	for i,char in enumerate(val):
		res += ord(char) * (10 ** i)
	return res


def processStep(num):
	for target,_ in enumerate(positions): # target
		for other,_ in enumerate(positions): # others that affect target
			if target == other:
				continue
			for d,_ in enumerate(velocity[target]):
				if positions[target][d] < positions[other][d]:
					velocity[target][d] += 1
				elif positions[target][d] > positions[other][d]:
					velocity[target][d] -= 1

	for i,_ in enumerate(positions):
		for d,_ in enumerate(positions[i]):
			positions[i][d] += velocity[i][d]

def calcState(num):
	strX1 = ''
	strY1 = ''
	strZ1 = ''
	for i,_ in enumerate(positions):
		if found[0] == 0:
			strX1 += str(positions[i][0]) + ';' + str(velocity[i][0]) + ';'
		if found[1] == 0:
			strY1 += str(positions[i][1]) + ';' + str(velocity[i][1]) + ';'
		if found[2] == 0:
			strZ1 += str(positions[i][2]) + ';' + str(velocity[i][2]) + ';'

	strX = strToNum(strX1)
	strY = strToNum(strY1)
	strZ = strToNum(strZ1)

	if found[0] == 0:
		if strX in statesX:
			delta = num - statesX.index(strX) - 1
			print('Loop for X = ' + str(delta) + ' start at ' + str(statesX.index(strX)))
			found[0] = delta
		else:
			statesX.append(strX)
	if found[1] == 0:
		if strY in statesY:
			delta = num - statesY.index(strY) - 1
			print('Loop for Y = ' + str(delta) + ' start at ' + str(statesY.index(strY)))
			found[1] = delta
		else:
			statesY.append(strY)

	if found[2] == 0:
		if strZ in statesZ:
			delta = num - statesZ.index(strZ) - 1
			print('Loop for Z = ' + str(delta) + ' start at ' + str(statesZ.index(strZ)))
			found[2] = delta
		else:
			statesZ.append(strZ)

def calcEnergy():
	kin = [0,0,0,0]
	pot = [0,0,0,0]
	total = 0
	for i,_ in enumerate(positions):
		for d,_ in enumerate(positions[i]):
			pot[i] += abs(positions[i][d])
			kin[i] += abs(velocity[i][d])
		total += kin[i] * pot[i]
	return pot,kin,total

# energies[0] = calcEnergy()
# states[0] = {
# 	'pos': deepcopy(positions),
# 	'vel': deepcopy(velocity)
# }

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)

num = 0
# for i in range(3000):
while True:
	num += 1
	processStep(num)
	if num % 1000 == 0:
		print(num)

	calcState(num)
	if found[0] != 0 and found[1] != 0 and found[2] != 0:
		break

print(lcm(lcm(found[0], found[1]), found[2]))
	# pos1 = str(positions[0][0]) + ';' + str(positions[0][1]) + ';' + str(positions[0][2])
	# if pos1 in poses1:
	# 	print('---- ' + str(num))
	# 	print(pos1)
	# 	print(num - poses1.index(pos1))
	# poses1.append(pos1)
	# if calcState():
	# 	print(num - 1)
	# 	exit(1)
	# for k,_ in enumerate(energies):
	# 	if k == num:
	# 		continue
	# 	isSame = False
	# 	if energies[k] == energies[num]:
	# 		isSame = True
	# 		for p,_ in enumerate(positions):
	# 			for d,_ in enumerate(positions[p]):
	# 				if states[k]['pos'][p][d] != positions[p][d]:
	# 					isSame = False
	# 	if isSame:
	# 		print(num)
	# 		print(states[k])
	# 		print(positions)
	# 		print(velocity)
	# 		exit(1)


# processStep()
# print(positions)
# print(velocity)
# print('=========== 1')
# processStep()
# print(positions)
# print(velocity)
# print('=========== 2')
# processStep()
# print(positions)
# print(velocity)
# print('=========== 3')
# processStep()
# print(positions)
# print(velocity)
# print('=========== 4')
# processStep()
# print(positions)
# print(velocity)
# print('=========== 5')