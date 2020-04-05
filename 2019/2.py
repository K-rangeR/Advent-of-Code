#!/usr/bin/env python3
import sys
import copy

def mul(a, b):
	return a * b

def add(a, b):
	return a + b

def perform_opcode(data, operand_one, operand_two, operation, res_pos):
	res = operation(data[operand_one], data[operand_two])
	data[res_pos] = res

test = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]

def run(tmp, noun, verb):
	tmp[1], tmp[2] = noun, verb
	i = 0
	while True:
		opcode = tmp[i] 
		if opcode == 99:
			break

		operand_one = tmp[i+1]
		operand_two = tmp[i+2]
		res_pos = tmp[i+3]

		if opcode == 1:
			perform_opcode(tmp, operand_one, operand_two, add, res_pos)
		elif opcode == 2:
			perform_opcode(tmp, operand_one, operand_two, mul, res_pos)
		else:
			print('opcode not known:', opcode)
			sys.exit(1)
		
		i += 4
	
	return tmp[0]

def solve():
	for noun in range(100):
		for verb in range(100):
			tmp = copy.deepcopy(test)
			if run(tmp, noun, verb) == 19690720:
				print(100 * noun + verb)
				sys.exit(0)
	
	print('not found')

solve()
