orbs = {'COM' : {'orbs_before': 0}}
lines  = []

data_file = open('data-06.txt', 'r', encoding="utf8")
line = data_file.readline()
while line:
	vals = line.rstrip().split(')')
	if not vals[0] in orbs:
		lines.append(line)
		line = data_file.readline()
		continue
	if not vals[1] in orbs:
		orbs[vals[1]] = {}
	print(vals[0], ' <- ', vals[1])
	orbs[vals[1]]['orbs_before'] = orbs[vals[0]]['orbs_before'] + 1
	orbs[vals[1]]['parent'] = vals[0]
	line = data_file.readline()

while len(lines) > 0:
	for _,line in enumerate(lines):
		vals = line.rstrip().split(')')
		if not vals[0] in orbs:
			continue
		if not vals[1] in orbs:
			orbs[vals[1]] = {}
		print(vals[0], ' <- ', vals[1])
		orbs[vals[1]]['orbs_before'] = orbs[vals[0]]['orbs_before'] + 1
		orbs[vals[1]]['parent'] = vals[0]
		lines.remove(line)

sum = 0

path_y = []
path_s = []

you_p = 'YOU'
san_p = 'SAN'

while you_p != 'COM':
	path_y.append(you_p)
	you_p = orbs[you_p]['parent']

path_y.append('COM')

while not san_p in path_y:
	path_s.append(san_p)
	san_p = orbs[san_p]['parent']

print(san_p)
print(path_s)
print(path_y)

sum = orbs['YOU']['orbs_before'] + orbs['SAN']['orbs_before'] - 2 * orbs[san_p]['orbs_before'] - 2

print(sum)
# for _,orb in enumerate(orbs):
# 	print(orb, orbs[orb]['orbs_before'])
# 	sum += orbs[orb]['orbs_before']

# print(sum)