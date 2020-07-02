#include <iostream>
#include <fstream>

inline int fuel(int mass)
{
  return (mass / 3) - 2;
}

int main()
{
  std::ifstream input("01_input.txt"); 
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 0;
  }

  int total_fuel = 0;
  std::string line;
  while (std::getline(input, line)) {
    total_fuel += fuel(atoi(line.c_str()));
  }

  std::cout << "Part #1: " << total_fuel << "\n";
  input.close();
  return 0;
}
