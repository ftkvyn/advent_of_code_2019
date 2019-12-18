programm_original = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,69,55,225,1001,144,76,224,101,-139,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,49,225,1102,51,78,225,1101,82,33,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,69,5,225,2,39,13,224,1001,224,-4140,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,101,42,44,224,101,-120,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,68,49,224,101,-3332,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,50,27,225,1102,5,63,225,1002,139,75,224,1001,224,-3750,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,102,79,213,224,1001,224,-2844,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1,217,69,224,1001,224,-95,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,36,37,225,1101,26,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,449,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

def getInput():
	return 5

def setOutupt(val):
	print(val)

# returns command, array of params
def getCommandAndParams(command):
	command_str = str(command)
	while len(command_str) < 5:
		command_str = '0' + command_str
	command_val = int(command_str[-2:])
	params = [int(command_str[-3:-2]), int(command_str[-4:-3]), int(command_str[-5:-4])]
	return command_val, params

def getArg(num, param, programm):
	if param == 0:
		return programm[num]
	else:
		return num

# returns is_end, next_pos
def run_command(pos, programm):
	command_raw = programm[pos]
	command, params = getCommandAndParams(command_raw)
	if command == 99:
		return True, pos + 1
	arg1_pos = programm[pos + 1]
	if command == 3:
		programm[arg1_pos] = getInput()
		return False, pos + 2
	elif command == 4:
		setOutupt(getArg(arg1_pos, params[0], programm))
		return False, pos + 2

	arg2_pos = programm[pos + 2]

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

	target = programm[pos + 3]

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
	memory = programm_original.copy()
	pos = 0

	is_end = False
	while not is_end:
		is_end, pos = run_command(pos, memory)
		if pos == -1:
			return -1

	return memory[0]

run_program()