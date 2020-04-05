import sys
from enum import Enum


class Operands:
	def __init__(self, operandOne, operandTwo, outputOperand):
		self.operandOne = operandOne
		self.operandTwo = operandTwo
		self.outputOperand = outputOperand


class IntCodeInstr:
	def __init__(self, opcode, operands):
		self._opcode = opcode
		self._operands = operands


	def getOpcode(self):
		return self._opcode
	

	def getOperandOne(self):
		return self._operands.operandOne


	def getOperandTwo(self):
		return self._operands.operandTwo

	
	def getOutputOperand(self):	
		return self._operands.outputOperand


class IntCodeVM:
	instr_operands_map = {
		1: 4,
		2: 4,
		3: 2,
		4: 2,
		5: 3,
		6: 3,
		7: 4,
		8: 4,
		9: 2,
	}

	def __init__(self, file_name):
		self.file_name = file_name
		self._code = []
		self._ip = 0
		self._rel_base = 0
		self._mem = {}


	def load(self):
		with open(self.file_name, 'r') as f:
			for line in f:
				instrs = line.split(',')
				self._code.extend(instrs)

	
	def run(self):
		while True:
			instr = self._decode(self._fetch())
			'''
			print(instr.getOpcode())
			print(instr.getOperandOne())
			print(instr.getOperandTwo())
			print(instr.getOutputOperand())
			print('======================')
			'''
			ipUpdate = self._execute(instr)
			self._updateIP(ipUpdate)


	def _fetch(self):
		return self._code[self._ip]
	

	def _decode(self, instr):
		instr = self._padInstruction(instr)
		opcode = self._getOpcode(instr)
		addrModes = self._getAddrModeForInstr(instr)

		if opcode == 3 or opcode == 4:
			# addr of the src or dst
			operandOne = self._getOperandData(addrModes, operand=1)
			operands = Operands(operandOne, None, None)
			return IntCodeInstr(opcode, operands)
		elif opcode == 99:
			return IntCodeInstr(opcode, None)
		elif opcode == 5 or opcode == 6:
			operandOne = self._getOperandData(addrModes, operand=1)
			operandTwo = self._getOperandData(addrModes, operand=2)
			operands = Operands(operandOne, operandTwo, None)
			return IntCodeInstr(opcode, operands)
		elif opcode == 9:
			operandOne = self._getOperandData(addrModes, operand=1)
			operands = Operands(operandOne, None, None)
			return IntCodeInstr(opcode, operands)

		
		# assume a three operand instruction
		outputAddr = int(self._code[self._ip+3])
		operandTwo = self._getOperandData(addrModes, operand=2)
		operandOne = self._getOperandData(addrModes, operand=1)
		operands = Operands(operandOne, operandTwo, outputAddr)
		return IntCodeInstr(opcode, operands)


	def _padInstruction(self, instr):
		return ('0' * (5 - len(instr))) + instr

	
	def _getOpcode(self, instr):
		return int(instr[-2:])

	
	def _getAddrModeForInstr(self, instr):
		return instr[:3]

	
	def _getOperandData(self, addrModes, operand):
		addrMode = int(addrModes[2]) if (operand == 1) else int(addrModes[1])
		if addrMode == 1: # immdiate
			return int(self._code[self._ip+operand])
		elif addrMode == 0: # position mode
			addr = int(self._code[self._ip+operand])
			# HACK
			if addr >= len(self._code):
				if addr in self._mem:
					return self._mem[addr]
				else:
					return 0
			return int(self._code[addr])
		elif addrMode == 2: # relative mode
			mode = int(self._code[self._ip + operand])
			addr = self._rel_base + mode
			return addr
		else:
			print('unknown addr mode:', addrMode)
			sys.exit(1)


	def _execute(self, instr):
		opcode = instr.getOpcode()
		if opcode == 1:
			return self._add(instr)
		elif opcode == 2:
			return self._mul(instr)
		elif opcode == 3:
			return self._input(instr)
		elif opcode == 4:
			return self._output(instr)
		elif opcode == 5:
			return self._jumpIfTrue(instr)
		elif opcode == 6:
			return self._jumpIfFalse(instr)
		elif opcode == 7:
			return self._lessThan(instr)
		elif opcode == 8:
			return self._equals(instr)
		elif opcode == 9:
			return self._update_rel_base(instr)
		elif opcode == 99:
			print('all done')
			sys.exit(0)
		else:
			print('unknown opcode:', opcode)
			sys.exit(1)

	
	def _add(self, instr):
		a = instr.getOperandOne()
		b = instr.getOperandTwo()
		s = int(a) + int(b)
		self._store(instr, s)
		return self._getNewIP(instr)


	def _mul(self, instr):
		a = instr.getOperandOne()
		b = instr.getOperandTwo()
		p = a * b
		self._store(instr, p)
		return self._getNewIP(instr)


	def _store(self, instr, value):
		addr = instr.getOutputOperand()
		if addr >= len(self._code):
			self._mem[addr] = str(value)
		else:
			self._code[addr] = str(value)


	def _input(self, instr):
		addr = instr.getOperandOne()
		val = input('Enter a number: ')
		if addr >= len(self._code):
			self._mem[addr] = str(val)
		else:
			self._code[addr] = str(val)
		return self._getNewIP(instr)


	def _output(self, instr):
		val = instr.getOperandOne()
		if val >= len(self._code) and val in self._mem:
			val = self._mem[val]
		print(val)
		return self._getNewIP(instr)

	
	def _jumpIfTrue(self, instr):
		if instr.getOperandOne():
			return instr.getOperandTwo()
		return self._getNewIP(instr)


	def _jumpIfFalse(self, instr):
		if not instr.getOperandOne():
			return instr.getOperandTwo()
		return self._getNewIP(instr)


	def _lessThan(self, instr):
		if instr.getOperandOne() < instr.getOperandTwo():
			self._code[instr.getOutputOperand()] = 1
		else:
			self._code[instr.getOutputOperand()] = 0
		return self._getNewIP(instr)


	def _equals(self, instr):
		if instr.getOperandOne() == instr.getOperandTwo():
			self._code[instr.getOutputOperand()] = 1
		else:
			addr = instr.getOutputOperand()
			if addr >= len(self._code):
				self._mem[addr] = 0
			else:
				self._code[addr] = 0
		return self._getNewIP(instr)


	def _update_rel_base(self, instr):
		self._rel_base += int(instr.getOperandOne())
		return self._getNewIP(instr)

	
	def _getNewIP(self, instr):
		return self.instr_operands_map[instr.getOpcode()] + self._ip


	def _updateIP(self, to):
		self._ip = to
