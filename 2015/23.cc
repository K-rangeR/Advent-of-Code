#include <iostream>
#include <fstream>
#include <unordered_map>
#include <regex>
#include <string>
#include <sstream>

struct Cpu {
  int ip; 
  std::unordered_map<std::string, int> registers;

  Cpu() : ip(0), registers{{"a",0}, {"b",0}} {}
};

std::regex offset_pattern("(\\+|\\-)(\\d+)");


void exe_hlf(Cpu& cpu, const std::string& reg) {
  if (cpu.registers.find(reg) == cpu.registers.end()) {
    std::cerr << "[hlf] Unknown register " << reg << "\n";
    exit(1);
  }
  cpu.registers[reg] /= 2;
  cpu.ip++;
}


void exe_tpl(Cpu& cpu, const std::string& reg) {
  if (cpu.registers.find(reg) == cpu.registers.end()) {
    std::cerr << "[tpl] Unknown register " << reg << "\n";
    exit(1);
  }
  cpu.registers[reg] *= 3;
  cpu.ip++;
}


void exe_inc(Cpu& cpu, const std::string& reg) {
  if (cpu.registers.find(reg) == cpu.registers.end()) {
    std::cerr << "[inc] Unknown register " << reg << "\n";
    exit(1);
  }
  cpu.registers[reg] += 1;
  cpu.ip++;
}


void exe_jmp(Cpu& cpu, const std::string& offset) {
  std::smatch args;
  if (!std::regex_match(offset, args, offset_pattern)) {
    std::cerr << "[jmp] Could not match offset_pattern: " << offset << "\n";
    exit(1);
  }

  if (args.str(1) == "+") {
    cpu.ip += std::atoi(args.str(2).c_str());
  } else {
    cpu.ip -= std::atoi(args.str(2).c_str());
  }
}


void exe_jie(Cpu& cpu, std::string& reg, const std::string& offset) {
  reg.pop_back();
  if (cpu.registers.find(reg) == cpu.registers.end()) {
    std::cerr << "[jie] Uknown register: " << reg << "\n";
    exit(1);
  }

  std::smatch args;
  if (!std::regex_match(offset, args, offset_pattern)) {
    std::cerr << "[jie] Could not match patter: " << offset << "\n";
    exit(1);
  }

  if (cpu.registers[reg] % 2 != 0) {
    cpu.ip++;
    return;
  }

  if (args.str(1) == "+") {
    cpu.ip += std::atoi(args.str(2).c_str());
  } else {
    cpu.ip -= std::atoi(args.str(2).c_str());
  }
}


void exe_jio(Cpu& cpu, std::string& reg, const std::string& offset) {
  reg.pop_back();
  if (cpu.registers.find(reg) == cpu.registers.end()) {
    std::cerr << "[jio] Uknown register: " << reg << "\n";
    exit(1);
  }

  std::smatch args;
  if (!std::regex_match(offset, args, offset_pattern)) {
    std::cerr << "[jio] Could not match patter: " << offset << "\n";
    exit(1);
  }

  if (cpu.registers[reg] != 1) {
    cpu.ip++;
    return;
  }

  if (args.str(1) == "+") {
    cpu.ip += std::atoi(args.str(2).c_str());
  } else {
    cpu.ip -= std::atoi(args.str(2).c_str());
  }
}


int main() {
  std::ifstream input("23_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  Cpu cpu;
  std::string instr;
  std::vector<std::string> instructions{};
  while (std::getline(input, instr)) {
    instructions.push_back(instr);
  }

  while (cpu.ip < instructions.size()) {
    std::stringstream ss;
    ss << instructions[cpu.ip];
    std::string opcode, p_one, p_two; 
    ss >> opcode >> p_one >> p_two;

    if (opcode == "hlf") {
      exe_hlf(cpu, p_one);
    } else if (opcode == "tpl") {
      exe_tpl(cpu, p_one);      
    } else if (opcode == "inc") {
      exe_inc(cpu, p_one); 
    } else if (opcode == "jmp") {
      exe_jmp(cpu, p_one);
    } else if (opcode == "jie") {
      exe_jie(cpu, p_one, p_two);      
    } else if (opcode == "jio") {
      exe_jio(cpu, p_one, p_two); 
    } else {
      std::cerr << "Unknown opcode: " << opcode << "\n";
      exit(1);
    }
    
    /*
    std::cout << "ip: " << cpu.ip
              << " a: " << cpu.registers["a"]
              << " b: " << cpu.registers["b"] << "\n";
    */
  }

  std::cout << "Answer: " << cpu.registers["b"] << "\n";
  input.close();
  return 0;
}
