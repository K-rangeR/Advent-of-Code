#!/usr/bin/env python3
import intcode

computer = intcode.IntCodeVM('tmp.txt')
computer.load()
computer.run()
