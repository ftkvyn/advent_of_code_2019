import os
import readchar
clear = lambda: os.system('cls')

field = {}
rows = [0,40]
cols = [0,40]

start = [0,0]
end = [0,0]

def setFieldVal(posy, posx, val):
	global field, rows, cols
	if not posy in field:
		field[posy] = {}
	field[posy][posx] = val

def printField():
	global field, droidPos, cols, rows
	field_str = ''
	for row in range(rows[0], rows[1] + 1):
		for col in range(cols[0], cols[1] + 1):
			if not row in field:
				field[row] = {}
			if not col in field[row]:
				field[row][col] = -1
			if start[0] == row and start[1] == col:
				field_str += 'S'
			elif end[0] == row and end[1] == col:
				field_str += 'D'
			else:
				if field[row][col] == 0: # empty
					field_str += '.'
				elif field[row][col] == -1: # wall
					field_str += '#'
				else:
					field_str += str(field[row][col] % 10)
		field_str += '\n'
	clear()
	print(field_str)

data_file = open('data-15.txt', 'r', encoding="utf8")
line = data_file.readline()
lineNum = 0
while line:
	for i in range(cols[0], cols[1]):
		val = -1
		if len(line) > i:
			if line[i] == '.':
				val = 0
			elif line[i] == 'S':
				start = [lineNum, i]
				val = 0
			elif line[i] == 'D':
				end = [lineNum, i]
				val = 0
		setFieldVal(lineNum, i, val)
	lineNum += 1
	line = data_file.readline()


# printField()
# input('')

end_found = False
move = 0
next_steps = [end]

def findNextSteps(step):
	result = []
	if field[step[0]-1][step[1]] == 0:
		result.append([step[0]-1, step[1]])

	if field[step[0]+1][step[1]] == 0:
		result.append([step[0]+1, step[1]])

	if field[step[0]][step[1]-1] == 0:
		result.append([step[0], step[1]-1])

	if field[step[0]][step[1]+1] == 0:
		result.append([step[0], step[1]+1])

	return result

while len(next_steps) > 0:
	move_result = []
	for i,step in enumerate(next_steps):
		# if step[0] == end[0] and step[1] == end[1]:
		# 	print('=========== FOUND ============')
		# 	print(move)
		# 	input('')
		# 	end_found = True
		setFieldVal(step[0], step[1], move)
		result = findNextSteps(step)
		move_result.extend(result)
	move += 1
	next_steps = move_result
	printField()

print(move)

# 391 too much