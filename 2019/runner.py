#!/usr/bin/env python3
from intcode import IntCode_VM, Memory, Operand, Operands, Input, Add, Output, Terminate, Mul, Equals, Less_Than

vm = IntCode_VM('dummy_intcode.txt')
mem = Memory()

# input, input, equal, less than, output, end
o1 = Operands(None, None, Operand(True, 10))
in1 = Input(3, o1, mem)

o2 = Operands(None, None, Operand(True, 11))
in2 = Input(3, o2, mem)

o3 = Operands(Operand(False, 10), Operand(False, 11), Operand(True, 20))
equal = Equals(8, o3, mem)

o4 = Operands(None, None, Operand(False, 20))
output = Output(4, o4, mem)

less_than = Less_Than(7, o3, mem)

output2 = Output(4, o4, mem)

o5 = Operands(Operand(True, 50), Operand(True, 40), Operand(True, 25))
less_than_2 = Less_Than(7, o5, mem)

o6 = Operands(None, None, Operand(False, 25))
output3 = Output(4, o6, mem)

o7 = Operands(Operand(False, 10), Operand(False, 11), Operand(True, 25))
mul = Mul(1, o7, mem)

end = Terminate(99, None, mem)

vm._code.extend([in1, in2, equal, output, less_than, output2, 
                 less_than_2, output3, mul, output3, end])
vm.run()
