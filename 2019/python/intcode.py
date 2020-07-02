from enum import Enum
from typing import Tuple, Type, List
import sys


class Addr_Mode(Enum):
  immidate = 1
  position = 2
  relative = 3

'''
Defines a mapping from the opcode to the number of operands it
has plus one. Used to update the instruction pointer and parse the intcode
code.
'''
operands_per_opcode = {
  1: 4, # add
  2: 4, # mul
  3: 2, # input
  4: 2, # output
  5: 3, # jump if true
  6: 3, # jump if false
  7: 4, # less than
  8: 4, # equals
  9: 2, # adjusts the relative base
}

'''
Represents the memory of the intcode computer
'''
class Memory:
  def __init__(self):
    self._mem = dict()

  
  def read(self, addr: int) -> int:
    if addr in self._mem:
      return self._mem[addr]
    else:
      print('POSSIBLE ERROR: Memory.read: address not found:', addr)
      return -1

  
  def write(self, addr: int, val: int):
    self._mem[addr] = val


'''
Represents the VM that will manage the execution of intcode instructions
'''
class IntCode_VM:
  def __init__(self, code_file: str):
    self._code_file = code_file
    self._code = []
    self._mem = Memory()
    self._ip = 0
    self._rel_base = 0


  def load(self):
    pass

  
  def run(self):
    '''
    parser = IntCode_Parser(self._code)
    parsed_code = parser.parse(self._mem)
    '''
    while True:
      cur_instr = self._code[self._ip]
      self._ip += cur_instr.run()


'''
Represents an operand, is_data is true if val is data, else it is false
because val is an address
'''
class Operand:
  def __init__(self, is_data: bool, val: int):
    self._is_data = is_data
    self._val = val


  def is_data(self) -> bool:
    return self._is_data


  def get_val(self, mem: Type[Memory]) -> int:
    if self.is_data():
      return self._val
    else:
      return mem.read(self._val)
    

'''
Represents an instructions operands
'''
class Operands:
  def __init__(self, \
               one:Type[Operand], \
         two:Type[Operand], \
         output:Type[Operand]):
    self._one = one
    self._two = two
    self._output = output


  def get_operand_one(self) -> Type[Operand]:
    return self._one

  
  def get_operand_two(self) -> Type[Operand]:
    return self._two


  def get_output_operand(self) -> Type[Operand]:
    return self._output

  
  def get_all(self, mem: Type[Memory]) -> Tuple[Type[Operand],...]:
    return (self._one.get_val(mem), 
            self._two.get_val(mem),
        self._output.get_val(mem))


'''
Represents a base intcode instruction
  * have a run method that returns a result of running the
    instruction and a change to make to the instruction pointer
'''
class IntCode_Instr:
  def __init__(self, opcode: int, operands: Type[Operands], mem: Type[Memory]):
    self._opcode = opcode
    self._operands = operands
    self._mem = mem

  
  '''
  Has the effect of running the instruction and storing its result
  into the memory
  '''
  def run(self) -> int:
    print('i should not be running: base.run()')
    return 0

  
  '''
  Returns the number to add the instruction pointer so that it jumps
  to the next instruction
  '''
  def get_ip_update(self) -> int:
    return operands_per_opcode[self._opcode]
    

'''
Represents the add instruction
'''
class Add(IntCode_Instr):
  def run(self) -> int:
    o1, o2, addr = self._operands.get_all(self._mem)
    result = o1 + o2
    self._mem.write(addr, result)
    return 1


'''
Represents the mul instruction
'''
class Mul(IntCode_Instr):
  def run(self) -> int:
    o1, o2, addr = self._operands.get_all(self._mem)
    result = o1 * o2
    self._mem.write(addr, result)
    return 1


'''
Represents the input instruction
'''
class Input(IntCode_Instr):
  def run(self) -> int:
    addr = self._operands.get_output_operand().get_val(self._mem)
    data = int(input('Enter a number: ').strip())
    self._mem.write(addr, data)
    return 1


'''
Represents the output instruction
'''
class Output(IntCode_Instr):
  def run(self) -> int:
    o1 = self._operands.get_output_operand().get_val(self._mem)
    print(o1)
    return 1


'''
Represents the jump if true instruction
'''
class Jump_If_True(IntCode_Instr):
  def run(self) -> int:
    test = self._operands.get_operand_one().get_val(self._mem)
    o2 = self._operands.get_operand_two().get_val(self._mem)
    return o2 if test else 1


'''
Represents the jump if false instruction
'''
class Jump_If_False(IntCode_Instr):
  def run(self) -> int:
    test = self._operands.get_operand_one().get_val(self._mem)
    o2 = self._operands.get_operand_two().get_val(self._mem)
    return o2 if not test else 1


'''
Represents the less than instruction
'''
class Less_Than(IntCode_Instr):
  def run(self) -> int:
    o1, o2, addr = self._operands.get_all(self._mem)
    res = 1 if o1 < o2 else 0
    self._mem.write(addr, res)
    return 1


'''
Represents the equals instruction
'''
class Equals(IntCode_Instr):
  def run(self) -> int:
    o1, o2, addr = self._operands.get_all(self._mem)
    res = 1 if o1 == o2 else 0
    self._mem.write(addr, res)
    return 1


'''
Represents the terminating instruction (99)
'''
class Terminate(IntCode_Instr):
  def run(self) -> int:
    print('terminating intcode program...')
    sys.exit(0)


'''
Creates a list of intcode instructions from intcode src code
'''
class IntCode_Parser:
  MAX_INSTR_LEN = 5
  INSTR_PADDING = '0'

  # Fully parsed code
  Code = List[Type[IntCode_Instr]]

  '''
  Reprsents the mapping between addressing mode an the function
  to parse instructions using that addressing mode
  '''
  addr_mode_map = {
    Addr_Mode.immidate: None,
    Addr_Mode.position: None,
    Addr_Mode.relative: None,
  }


  def __init__(self, code: List[str]):
    self._code = code


  def parse(self, memory: Type[Memory]) -> Code:
    pass

  
  '''
  Pads the instruction to the max length
  '''
  def _pad_instr(self, instr: str):
    return (INSTR_PADDING * (MAX_INSTR_LEN - len(instr))) + instr

  
  def _parse_immdiate_addr_mode(self, instr: str) -> Type[Operand]:
    pass


  def _parse_position_addr_mode(self, instr: str) -> Type[Operand]:
    pass
