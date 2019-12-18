programm_original = [3,8,1001,8,10,8,105,1,0,0,21,42,55,64,85,98,179,260,341,422,99999,3,9,101,2,9,9,102,5,9,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]

program_states = []

mem = 0
phases = []
phaseProvided = [False, False, False, False, False]

def getInput():
	global mem, phaseNum, phases, phaseProvided
	# print('get input for ' + str(phaseNum))
	if phaseProvided[phaseNum]:
		# print('memory - ' + str(mem))
		return mem
	else:
		# print('phase - ' + str(phases[phaseNum]))
		phaseProvided[phaseNum] = True
		return phases[phaseNum]

def setOutupt(val):
	global mem, phaseNum
	mem = val
	# print('>>>output from ' + str(phaseNum) + ' = ' + str(mem))

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
		return True, pos + 1, False
	arg1_pos = programm[pos + 1]
	if command == 3:
		programm[arg1_pos] = getInput()
		return False, pos + 2, False
	elif command == 4:
		setOutupt(getArg(arg1_pos, params[0], programm))
		return False, pos + 2, True

	arg2_pos = programm[pos + 2]

	if command == 5:
		if getArg(arg1_pos, params[0], programm) != 0:
			return False, getArg(arg2_pos, params[1], programm), False
		else:
			return False, pos + 3, False

	if command == 6:
		if getArg(arg1_pos, params[0], programm) == 0:
			return False, getArg(arg2_pos, params[1], programm), False
		else:
			return False, pos + 3, False

	target = programm[pos + 3]

	if command == 7:
		if getArg(arg1_pos, params[0], programm) < getArg(arg2_pos, params[1], programm):
			programm[target] = 1
		else:
			programm[target] = 0
		return False, pos + 4, False

	if command == 8:
		if getArg(arg1_pos, params[0], programm) == getArg(arg2_pos, params[1], programm):
			programm[target] = 1
		else:
			programm[target] = 0
		return False, pos + 4, False

	if command == 1:
		programm[target] = getArg(arg1_pos, params[0], programm) + getArg(arg2_pos, params[1], programm)
	elif command == 2:
		programm[target] = getArg(arg1_pos, params[0], programm) * getArg(arg2_pos, params[1], programm)
	else: 
		return True, -1, False
	return False, pos + 4, False

# returns result
def run_program(state):
	is_end = False
	while not is_end:
		is_end, state['pos'], is_output = run_command(state['pos'], state['prog'])
		if state['pos'] == -1:
			return -1
		if is_output:
			return 1

	return 0

max_mem = 0
max_phases = []

def try_phases(phases_att):
	global mem, phases, phaseNum, phaseProvided, max_mem, max_phases
	phases = phases_att.copy()
	program_states = []
	mem = 0
	phaseProvided = [False, False, False, False, False]
	is_ended = False
	while not is_ended:
		for num,_ in enumerate(phases):
			phaseNum = num
			# print('================= phase ' + str(num))
			if len(program_states) < num + 1:
				program_states.append({
					'prog': programm_original.copy(),
					'pos': 0
				})
			code = run_program(program_states[num])
			if code == 1:
				# handle output - run next controller
				continue
			if code == 0:
				# end programm
				is_ended = True
			if code == -1:
				print('error')
	# print(mem)
	if mem > max_mem:
		max_mem = mem
		max_phases = phases.copy()

# try_phases([9,7,8,5,6])
for p1 in range(5,10):
	for p2 in range(5,10):
		if p1 == p2:
			continue
		for p3 in range(5,10):
			if (p3 == p2) or (p3 == p1):
				continue
			for p4 in range(5,10):
				if (p4 == p1) or (p4 == p2) or (p4 == p3):
					continue
				for p5 in range(5,10):
					if (p5 == p1) or (p5 == p2) or (p5 == p3) or (p5 == p4):
						continue
					try:
						try_phases([p1,p2,p3,p4,p5])
					except:
						print('error')

print(max_mem)
print(max_phases)