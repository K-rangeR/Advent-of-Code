#!/usr/bin/env python3
import intcode

computer = intcode.IntCodeVM('TEST.txt')
computer.load()
#computer._code = ['3','12','6','12','15','1','13','14','13','4','13','99','-1'
#                 ,'0','1','9']
#computer._code = ['3','3','1105','-1','9','1101','0','0','12','4','12','99','1']

#test = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
'''
for i in test:
  computer._code.append(str(i))
'''

computer.run()
