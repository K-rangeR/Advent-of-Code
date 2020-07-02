#!/usr/bin/env python3
import intcode
from subprocess import Popen, PIPE, STDOUT
from itertools import permutations
import shutil
import os

max_thrust = -1
perm = permutations([5, 6, 7, 8, 9])
for p in list(perm):
  input_sig = 0
  for phase_setting in p:
    shutil.copyfile('./input.txt', 'tmp.txt')
    proc = Popen(['./7.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    msg = '{}\n{}'.format(phase_setting, input_sig)
    input_sig = proc.communicate(input=msg.encode())[0].decode().strip()
    os.remove('tmp.txt')
  max_thrust = max(max_thrust, int(input_sig))

print(max_thrust)
