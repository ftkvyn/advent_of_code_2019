from termcolor import colored
import colorama
colorama.init()

cols = 1500
rows = 1000
# cols = 12
# rows = 12

field = {} # [[''] * cols for i in range(rows)]

# for ln in range(rows):
# 	field[ln] = {}
# 	for cn in range(cols):
# 		field[ln][cn] = {'char': '.', 'color': 'white', 'steps': {}}
min_collision_len = 9999999999

def printField():
	global field, cols, rows
	for ln in range(rows):
		for cn in range(cols):
			val = field[ln][cn] # val = {'char': '-', 'color': 'red'}
			if val['char'] == '.':
				print(val['char'], end='')
			else:
				print(colored(val['char'], val['color']), end='', )
		print('')
	print('')

def markField(x, y, char, color, steps):
	global x_start, y_start, min_collision_len
	if not y in field:
		field[y] = {}
	if not x in field[y]:
		field[y][x] = {'char': '.', 'color': 'white', 'steps': {}}

	if field[y][x]['char'] == 'o':
		return
	elif field[y][x]['char'] == '.':
		field[y][x]['char'] = char
		field[y][x]['color'] = color
		field[y][x]['steps'][color] = steps
	elif field[y][x]['color'] == color:
		field[y][x]['char'] = '+'
		return True
	else:
		field[y][x]['char'] = 'X'
		field[y][x]['color'] = 'red'
		field[y][x]['steps'][color] = steps
		# dist = abs(x - x_start) + abs(y - y_start)
		print(field[y][x]['steps'])
		sum = 0
		for _,step in enumerate(field[y][x]['steps']):
			sum += field[y][x]['steps'][step]
		print(sum)
		if(sum < min_collision_len):
			min_collision_len = sum
	return False

def buildLine(input, color):
	global field, cols, rows, x_start, y_start
	x0 = x_start
	y0 = y_start
	steps = -1
	for _,command in enumerate(input):
		direction = command[0]
		value = int(command[1:]) + 1
		if direction == 'R':
			char = '-'
			x = x0
			for i in range(value):
				x = x0 + i
				steps += 1
				is_turn = markField(x, y0, char, color, steps)
				if is_turn:
					steps -= 1
			x0 = x
		elif direction == 'U':
			char = '|'
			y = y0
			for i in range(value):
				y = y0 - i
				steps += 1
				is_turn = markField(x0, y, char, color, steps)
				if is_turn:
					steps -= 1
			y0 = y
		elif direction == 'L':
			char = '-'
			x = x0
			for i in range(value):
				x = x0 - i
				steps += 1
				is_turn = markField(x, y0, char, color, steps)
				if is_turn:
					steps -= 1
			x0 = x
		elif direction == 'D':
			char = '|'
			y = y0
			for i in range(value):
				y = y0 + i
				steps += 1
				is_turn = markField(x0, y, char, color, steps)
				if is_turn:
					steps -= 1
			y0 = y
		# printField()
		# print('===============')

x_start = int(cols / 2)
y_start = int(rows / 2)
field[y_start] = {}
field[y_start][x_start] = {'char': 'o', 'color': 'white'}


data_file = open('data-03.txt', 'r', encoding="utf8")

line = data_file.readline()
input = line.split(',')
buildLine(input, 'green')
# printField()

line = data_file.readline()
input = line.split(',')
buildLine(input, 'blue')

# printField()
print(min_collision_len)