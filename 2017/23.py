#!/usr/bin/env python3
from collections import defaultdict


def main():
  instrs = []
  with open('23_input.txt', 'r') as instr_file:
    for line in instr_file:
      instrs.append(line.strip().split(' ')) 
  
  regs = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
  isp, muls = 0, 0
  while 0 <= isp < len(instrs):
    instr = instrs[isp]
    opcode, operand1, operand2 = instr
    operand2 = decode_operand(operand2, regs)
    if opcode == 'set':
      regs[operand1] = operand2 
      isp += 1
    elif opcode == 'sub':
      regs[operand1] -= operand2
      isp += 1
    elif opcode == 'mul':
      regs[operand1] *= operand2
      muls += 1
      isp += 1
    elif opcode == 'jnz':
      operand1 = regs[operand1] if operand1 in regs else int(operand1)
      isp += operand2 if operand1 != 0 else 1

  print('Answer:', muls)
  

def decode_operand(operand, regs):
  try:
    op = int(operand)
    return op
  except ValueError as e:
    return regs[operand]


if __name__ == '__main__':
  main()
