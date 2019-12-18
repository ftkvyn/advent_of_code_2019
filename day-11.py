programm_original = [3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1007,14,10,2,1106,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,58,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,103,1,5,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,128,1,106,18,10,1,7,20,10,1006,0,72,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,164,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,186,1,1007,8,10,1006,0,98,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,216,2,102,8,10,1,1008,18,10,1,1108,8,10,1006,0,68,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,274,1,1105,7,10,101,1,9,9,1007,9,1060,10,1005,10,15,99,109,621,104,0,104,1,21102,936995738520,1,1,21102,316,1,0,1106,0,420,21101,0,936995824276,1,21102,1,327,0,1106,0,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,248129784923,1,1,21102,1,374,0,1105,1,420,21102,29015149735,1,1,21101,385,0,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21101,983925826304,0,1,21101,0,408,0,1105,1,420,21102,825012036364,1,1,21101,0,419,0,1105,1,420,99,109,2,22101,0,-1,1,21101,0,40,2,21101,0,451,3,21102,441,1,0,1105,1,484,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1101,0,0,446,109,-2,2105,1,0,0,109,4,2102,1,-1,483,1207,-3,0,10,1006,10,501,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21101,520,0,0,1106,0,525,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,567,0,1105,1,525,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,586,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21201,-1,0,1,21102,1,608,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

relative_base = 0

field = {}

point = [20,20]

if not point[0] in field:
	field[point[0]] = {}
field[point[0]][point[1]] = 1

direction = '^'

directionChange = {
	# turn right
	1: {
		'^': '>',
		'>': 'v',
		'<': '^',
		'v': '<',
	},
	# turn left
	0: {
		'^': '<',
		'>': '^',
		'<': 'v',
		'v': '>',
	}
}

move = {
	'^': [1,0],
	'>': [0,1],
	'<': [0,-1],
	'v': [-1,0],
}

paintedCells = []

isOutputColor = True

def getInput():
	if not point[0] in field:
		field[point[0]] = {}
	if not point[1] in field[point[0]]:
		field[point[0]][point[1]] = 0
	return field[point[0]][point[1]]

def setOutupt(val):
	global field, point, isOutputColor, direction, directionChange, move, paintedCells
	if isOutputColor:
		if not point[0] in field:
			field[point[0]] = {}
		field[point[0]][point[1]] = val
		# cellStr = str(point[0]) + ';' + str(point[1])
		# print(cellStr)
		# if not cellStr in paintedCells:
		# 	paintedCells.append(cellStr)
	else: 
		# change direction
		direction = directionChange[val][direction]
		moveDelta = move[direction]
		point[0] += moveDelta[0]
		point[1] += moveDelta[1]
	isOutputColor = not isOutputColor
	# print(val)

# returns command, array of params
def getCommandAndParams(command):
	command_str = str(command)
	while len(command_str) < 5:
		command_str = '0' + command_str
	command_val = int(command_str[-2:])
	params = [int(command_str[-3:-2]), int(command_str[-4:-3]), int(command_str[-5:-4])]
	return command_val, params

def getArg(num, param, programm):
	global relative_base
	if param == 0:
		if num in programm:
			return programm[num]
		else:
			return 0
	elif param == 1:
		return num
	elif param == 2:
		if (num + relative_base) in programm:
			return programm[num + relative_base]
		else:
			return 0

def setVal(num, param, programm, val):
	global relative_base
	if param == 0:
		programm[num] = val
	elif param == 2:
		programm[num + relative_base] = val

# returns is_end, next_pos
def run_command(pos, programm):
	global relative_base
	command_raw = getArg(pos, 0, programm)
	command, params = getCommandAndParams(command_raw)
	if command == 99:
		return True, pos + 1
	arg1_pos = getArg(pos + 1, 0, programm)
	if command == 3:
		setVal(arg1_pos, params[0], programm, getInput())
		return False, pos + 2
	elif command == 4:
		setOutupt(getArg(arg1_pos, params[0], programm))
		return False, pos + 2
	elif command == 9:
		relative_base += getArg(arg1_pos, params[0], programm)
		return False, pos + 2

	arg2_pos = getArg(pos + 2, 0, programm)

	if command == 5:
		if getArg(arg1_pos, params[0], programm) != 0:
			return False, getArg(arg2_pos, params[1], programm)
		else:
			return False, pos + 3

	if command == 6:
		if getArg(arg1_pos, params[0], programm) == 0:
			return False, getArg(arg2_pos, params[1], programm)
		else:
			return False, pos + 3

	target = getArg(pos + 3, 0, programm)
	if params[2] == 2:
		target += relative_base

	if command == 7:
		if getArg(arg1_pos, params[0], programm) < getArg(arg2_pos, params[1], programm):
			programm[target] = 1
		else:
			programm[target] = 0
		return False, pos + 4

	if command == 8:
		if getArg(arg1_pos, params[0], programm) == getArg(arg2_pos, params[1], programm):
			programm[target] = 1
		else:
			programm[target] = 0
		return False, pos + 4

	if command == 1:
		programm[target] = getArg(arg1_pos, params[0], programm) + getArg(arg2_pos, params[1], programm)
	elif command == 2:
		programm[target] = getArg(arg1_pos, params[0], programm) * getArg(arg2_pos, params[1], programm)
	else: 
		return True, -1
	return False, pos + 4

# returns result
def run_program():
	memory = {}
	for i,val in enumerate(programm_original):
		memory[i] = val
	# memory = programm_original.copy()
	pos = 0

	is_end = False
	while not is_end:
		is_end, pos = run_command(pos, memory)
		if pos == -1:
			return -1

	return memory[0]

run_program()

# print(paintedCells)
# print(len(paintedCells))
# 14-21
# 20-61
# for _,row in enumerate(field):
# 	for _,col in enumerate(field[row]):
for row in range(21,14,-1):
	for col in range(20,61):
		if not row in field:
			field[row] = {}
		if not col in field[row]:
			field[row][col] = 0
		if field[row][col] == 0:
			print(' ', end='')
		else:
			print('#', end='')
	print('')