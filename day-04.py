def is_good_nums(num):
	num_s = str(num)
	num_s = ' ' + num_s + ' '
	same_nums = False
	for j in range(5):
		i = j + 1
		if num_s[i] == num_s[i + 1]:
			if (num_s[i] == num_s[i - 1]) or (num_s[i] == num_s[i + 2]):
				same_nums = same_nums or False
			else:
				same_nums = True
		if num_s[i] > num_s[i + 1]:
			return False
	return same_nums

count = 0

# print(is_good_nums(112233))

for num in range(372037, 905157):
	if is_good_nums(num):
		count += 1

print(count)