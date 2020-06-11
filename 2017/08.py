#!/usr/bin/env python3
from collections import defaultdict
import sys


def cond_true(operand1, operator, operand2):
  operand1 = registers[operand1]
  if operator == '>':
    return operand1 > operand2
  elif operator == '>=':
    return operand1 >= operand2
  elif operator == '<':
    return operand1 < operand2
  elif operator == '<=':
    return operand1 <= operand2
  elif operator == '==':
    return operand1 == operand2
  elif operator == '!=':
    return operand1 != operand2
  else:
    print('Operator unknown', operator)
    sys.exit(1)


def exe_instr(operand1, intr_name, operand2):
  if intr_name == 'inc':
    registers[operand1] += operand2  
  elif instr_name == 'dec':
    registers[operand1] -= operand2  
  else:
    print('Unknown instr:', instr_name)
    sys.exit(1)


registers = defaultdict(lambda: 0, defaultdict(int))
with open('08_input.txt', 'r') as f:
  for line in f:
    instr = line.strip().split()
    operand1, operator, operand2 = instr[4:]
    if cond_true(operand1, operator, int(operand2)):
      instr_o1, instr_name, instr_o2 = instr[:3] 
      exe_instr(instr_o1, instr_name, int(instr_o2)) 

answer = max(registers.values())
print('Answer:', answer)
