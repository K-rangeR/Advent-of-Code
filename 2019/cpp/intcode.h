#ifndef INT_CODE
#define INT_CODE

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cstdlib>

class IntCodeComputer {
public:
  IntCodeComputer() = default;
  ~IntCodeComputer() = default;

  IntCodeComputer(IntCodeComputer& rhs) = delete;
  IntCodeComputer operator=(IntCodeComputer& rhs) = delete;

  // Returns 0 on success, -1 on fail
  int load_code(const std::string& file_name)
  {
    std::ifstream input(file_name); 
    if (!input) {
      return -1;
    }
    
    std::string token {};
    while (std::getline(input, token, ',')) {
      code.emplace_back(atoi(token.c_str()));
    }

    input.close();
    return 0;
  }

  void run()
  {
    write_to(12, 1); write_to(2,2);

    while (value_at(pc) != 99) {
      int opcode = value_at(pc); 
      int operand1 = decode_operand(value_at(pc+1)); 
      int operand2 = decode_operand(value_at(pc+2));
      int dest = value_at(pc+3);

      if (opcode == 1) {
        write_to(operand1 + operand2, dest);
      } else if (opcode == 2) {
        write_to(operand1 * operand2, dest);
      }

      pc += 4;
    }
  }

  int value_at(int index) { return code.at(index); }

private:
  void write_to(int data, int index) { code[index] = data; }
  int decode_operand(int operand) { return code[operand]; }

private:
  std::vector<int> code; 
  int pc = 0;
};

#endif
