import math

field = {}
lines  = []
rows = -1
asteroids = []

data_file = open('data-10.txt', 'r', encoding="utf8")
line = data_file.readline()
while line:
	rows += 1
	field[rows] = {}
	for i,ch in enumerate(line):
		if ch == '#':
			field[rows][i] = '#'
			asteroids.append([i, rows, 0])
		elif ch == '.':
			field[rows][i] = '.'
	line = data_file.readline()

def sign(x):
	if x == 0:
		return 0
	if x < 0:
		return -1
	if x > 0:
		return 1

def find_line(p1, p2):
	k = (p1[1] - p2[1])/(p1[0] - p2[0])
	b = p1[1] - k * p1[0]
	return k,b

# True if p2 hides p3 for p1
def is_between(p1, p2, p3):
	if p1[0] == p3[0]:
		if p2[0] != p1[0]:
			return False
		return sign(p1[1] - p2[1]) == sign(p2[1] - p3[1])
	if p1[1] == p3[1]:
		if p2[1] != p1[1]:
			return False
		return sign(p1[0] - p2[0]) == sign(p2[0] - p3[0])
	
	k,b = find_line(p1, p3)
	delta = math.fabs((k * p2[0] + b) - p2[1])
	if delta > 0.000001:
		return False

	return sign(p1[1] - p2[1]) == sign(p2[1] - p3[1])

def find_dist(p1, p2):
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	dist = math.sqrt(dx*dx + dy*dy)
	return dist

visible = []

def process_point(num):
	global point, visible
	target = asteroids[num]
	if target[0] == point[0] and target[1] == point[1]:
		return
	is_hidden = False
	for i,betw in enumerate(asteroids):
		if i == num:
			continue
		if betw[0] == point[0] and betw[1] == point[1]:
			continue
		if is_between(point, betw, target):
				# if (dest[0] == 5) and (dest[1] == 8):
					# print('------------')
					# print('(' + str(dest[0]) + ',' + str(dest[1]) + ')' 
					# + ' ==>== ' +
					# '(' + str(betw[0]) + ',' + str(betw[1]) + ')'
					# + ' ==>== ' +
					# '(' + str(target[0]) + ',' + str(target[1]) + ')')
					# print(target)
					# print('------------')
			is_hidden = True

	if not is_hidden:
		target[2] = math.atan2(point[1] - target[1], point[0] - target[0]) - (math.pi / 2)
		if target[2] < 0:
			target[2] += math.pi * 2
		visible.append(target)

# max_num = 0

point = [29, 28]
# point = [11, 13]
# point = [8, 3]

print(len(asteroids))
for num,_ in enumerate(asteroids):
	process_point(num)

def sortPoints(val):
    return val[2] 

# print(asteroids)
# print(asteroids[max_num])
visible.sort(key = sortPoints)
print(len(visible))
print(visible[0])
print(visible[1])
print(visible[2])
print(visible[19])
print(visible[29])
print(visible[49])
print(visible[198])
print('----------------')
print(visible[199])
