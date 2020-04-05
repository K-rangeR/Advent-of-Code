#!/usr/bin/env python3
import math
import sys

width = 25
height = 6
image = []

with open('input.txt', 'r') as f:
	line = f.readline().strip()
	layer = -1 
	for (i, digit) in enumerate(line):
		if i % (width * height) == 0:
			layer += 1
			image.append(list())
		image[layer].append(digit)

def f(pos, layer):
	global image
	if layer > len(image):
		print('whoops something is very wrong')
		sys.exit(1)
	if image[layer][pos] != '2':
		return image[layer][pos]
	
	return f(pos, layer+1)

res = []
for (i,top) in enumerate(image[0]):
	r = f(i, 0)
	res.append(r)

for (i, letter) in enumerate(res):
	if i % width == 0:
		print()
	if letter == '0':
		print(' ', end='')
	else:
		print(letter, end='')
