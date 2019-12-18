import math

pattern = [0,1,0,-1]
val = '03036732577212944063491565474664'
signal = list(map(int, val))
# offset = 5974057
offset = 303673
multiplier = 10000

def next_step():
	global signal
	new_signal = signal.copy()
	for i,_ in enumerate(signal):
		new_signal[i] = 0
		pos = 1 # to skip the first element in pattern
		for k,_ in enumerate(signal):
			pat = math.floor(pos / (i + 1)) % len(pattern)
			new_signal[i] += signal[k] * pattern[pat]
			pos += 1
		new_signal[i] = abs(new_signal[i]) % 10
	signal = new_signal

A = {}
ended = {}

def getPat(dig, i):
	pat = (math.floor( (i + 1) / (dig + 1))) % 4
	return pattern[pat]

def getDigit(step, dig):
	if dig >= len(signal) * multiplier:
		return 0
	if step == 0:
		return signal[dig % len(signal)]
	if not step in A:
		A[step] = {}
	if dig in A[step]:
		return A[step][dig]
	sum = 0
	N = math.ceil((len(signal) * multiplier + 1) / ((dig + 1) * 4))
	for n in range(N):
		for k in range(dig + 1):
			offset_before_group = (dig + 1) * 4 * n + (dig + 1) - 1 # n - number of patter repetition
			sum += getDigit(step - 1, k + offset_before_group)
			offset_inside_group = offset_before_group + 2 * (dig + 1)
			sum -= getDigit(step - 1, k + offset_inside_group)
	sum = abs(sum) % 10
	A[step][dig] = sum
	if not step in ended:
		ended[step] = True
		print('step ended = ' + str(step))
	return sum

step = 100

result = [getDigit(step, 0 + offset), getDigit(step, 1 + offset), getDigit(step, 2 + offset), getDigit(step, 3 + offset),
getDigit(step, 4 + offset),getDigit(step, 5 + offset),getDigit(step, 6 + offset),
getDigit(step, 7 + offset)]

print(result)