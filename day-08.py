data_file = open('data-08.txt', 'r', encoding="utf8")
line = data_file.readline()

layers = []

pos = 0

nums = []

def readLayer(num):
	global pos, layers, zeroes, ones, twos
	for col in range(6):
		for row in range(25):
			val = int(line[pos])
			layers[num][col][row] = val
			pos += 1
			nums[num][val] += 1

layer_num = 0
while pos < len(line):
	layers.append([[0] * 25 for i in range(6)])
	nums.append([0,0,0])
	readLayer(layer_num)
	layer_num += 1

img = [[0] * 25 for i in range(6)]

def getPixel(col, row):
	global layer_num, layers
	for num in range(layer_num):
		if layers[num][col][row] != 2:
			return layers[num][col][row]
	return 2

for col in range(6):
	for row in range(25):
		img[col][row] = getPixel(col, row)
		if img[col][row] == 0:
			print(' ', end='')
		if img[col][row] == 1:
			print('Ш', end='')
		if img[col][row] == 2:
			print('.', end='')
	print('')