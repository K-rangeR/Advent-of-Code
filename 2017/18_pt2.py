#!/usr/bin/env python3
from collections import defaultdict


class Process:
  def __init__(self, pid, code, recv_pipe, send_pipe):
    self.pid = pid
    self.code = code
    self.recv_pipe = recv_pipe
    self.send_pipe = send_pipe
    self.registers = defaultdict(lambda: 0, defaultdict(int))
    self.registers['p'] = self.pid
    self.isp = 0
    self.blocked = False
    self.data_sent = 0


  def exe_next_instr(self):
    instr = self.code[self.isp]
    opcode, operand_one, operand_two = self._decode_instr(instr)
    if opcode == 'snd':
      self.send_pipe.append(self._decode_operand(operand_one))
      self.data_sent += 1
      self.isp += 1
    elif opcode == 'set':
      self.registers[operand_one] = self._decode_operand(operand_two)
      self.isp += 1
    elif opcode == 'add':
      self.registers[operand_one] += self._decode_operand(operand_two)
      self.isp += 1
    elif opcode == 'mul':
      self.registers[operand_one] *= self._decode_operand(operand_two)
      self.isp += 1
    elif opcode == 'mod':
      self.registers[operand_one] %= self._decode_operand(operand_two)
      self.isp += 1
    elif opcode == 'rcv':
      if len(self.recv_pipe) == 0:
        self.blocked = True
      else:
        msg = self.recv_pipe.pop(0)
        self.registers[operand_one] = msg
        self.blocked = False
        self.isp += 1
    elif opcode == 'jgz':
      operand_one = self._decode_operand(operand_one)
      operand_two = self._decode_operand(operand_two)
      self.isp += operand_two if operand_one > 0 else 1
    else:
      print('Unknown opcode:', opcode)

    return self._ran_last_instr()


  def _decode_instr(self, instr):
    tokens = instr.split(' ')
    if len(tokens) == 3:
      return tokens
    elif len(tokens) == 2:
      return (tokens[0], tokens[1], -1)


  def _decode_operand(self, operand):
    try:
      val = int(operand)
      return val
    except ValueError as e:
      return self.registers[operand]


  def is_blocked(self):
    return self.blocked


  def _ran_last_instr(self):
    return self.isp < 0 or self.isp >= len(self.code)


class Duet_Scheduler:
  def __init__(self, instr_time_slice, p1, p2):
    self.instr_time_slice = instr_time_slice
    self.next_process = 0
    self.processes = [p1, p2]


  def run(self):
    while self.processes:
      curr_process = self.processes[self.next_process]
      time_slice = 0
      while time_slice < self.instr_time_slice:
        done = curr_process.exe_next_instr()
        if done:
          del self.processes[self.next_process]
          break
        time_slice += 1
      if self._in_deadlock():
        print('Deadlock detected!!!')
        return
      self.next_process = (self.next_process + 1) % len(self.processes)


  def _in_deadlock(self):
    if len(self.processes) == 1:
      return self.processes[0].is_blocked()
    elif len(self.processes) == 2:
      return self.processes[0].is_blocked() and self.processes[1].is_blocked()
    return False


with open('18_input.txt', 'r') as duet_instr:
  code = duet_instr.read().strip().split('\n')

pipe1 = []
pipe2 = []

process_one = Process(0, code, pipe1, pipe2)
process_two = Process(1, code, pipe2, pipe1)

scheduler = Duet_Scheduler(1, process_one, process_two)
scheduler.run()

print('Program 0 sent:', process_one.data_sent)
print('Program 1 sent:', process_two.data_sent)
