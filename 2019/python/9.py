#!/usr/bin/env python3
import intcode

vm = intcode.IntCodeVM('input.txt')
vm.load()
vm.run()
