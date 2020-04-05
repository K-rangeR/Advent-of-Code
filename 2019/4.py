#!/usr/bin/env python3
def non_decreasing_order(num):
	p, c = 0, 1
	while c < len(num):
		if num[c] < num[p]:
			return False
		p = c
		c += 1
	return True


def adjacent_repeated_digits(num):
	i = len(num) - 1
	while i > 0:
		if num[i] == num[i-1]:
			return True
		i -= 1
	return False


def case_three(num):
	c = {}
	for i in num:
		if i in c:
			c[i] += 1
		else:	
			c[i] = 1

	for (k, v) in c.items():
		if v == 2:
			return True
	return False

print(case_three('112233'))
print(case_three('123444'))
print(case_three('111122'))

count = 0
for pwd in range(277777, 779999+1):
	pwd = str(pwd)
	if non_decreasing_order(pwd) and adjacent_repeated_digits(pwd) and case_three(pwd):
		count += 1
	
print(count)
