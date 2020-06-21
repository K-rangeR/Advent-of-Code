#!/usr/bin/env python3
from collections import defaultdict


def main():
  with open('18_input.txt', 'r') as duet_data:
    instrs = duet_data.read().strip().split('\n')

  part_1(instrs)


def part_1(instrs):
  isp = 0
  regs = defaultdict(lambda: 0, defaultdict(int))
  last_sound_freq, recovered_freq = -1, -1
  while 0 <= isp < len(instrs):
    instr = instrs[isp]
    opcode, operand_one, operand_two = decode_instr(instr)
    if opcode == 'snd':
      last_sound_freq = decode_operand(operand_one, regs)
      isp += 1
    elif opcode == 'set':
      regs[operand_one] = decode_operand(operand_two, regs)
      isp += 1
    elif opcode == 'add':
      regs[operand_one] += decode_operand(operand_two, regs)
      isp += 1
    elif opcode == 'mul':
      regs[operand_one] *= decode_operand(operand_two, regs)
      isp += 1
    elif opcode == 'mod':
      regs[operand_one] %= decode_operand(operand_two, regs)
      isp += 1
    elif opcode == 'rcv':
      if regs[operand_one] != 0:
        recovered_freq = last_sound_freq
        break
      isp += 1
    elif opcode == 'jgz':
      isp += decode_operand(operand_two, regs) if regs[operand_one] > 0 else 1
    else:
      print('Unknown opcode:', opcode)

  print('Part #1:', recovered_freq)


def decode_instr(instr):
  tokens = instr.split(' ')
  if len(tokens) == 3:
    return tokens
  elif len(tokens) == 2:
    return (tokens[0], tokens[1], -1)


def decode_operand(operand, regs):
  try:
    val = int(operand)
    return val
  except ValueError as e:
    return regs[operand]
     

if __name__ == '__main__':
  main()
