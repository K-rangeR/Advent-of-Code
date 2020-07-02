#include <iostream>
#include <fstream>

inline int fuel(int mass)
{
  return (mass / 3) - 2;
}

inline int fuel_part2(int mass)
{
  int result = 0;
  while (true) {
    mass = fuel(mass);
    if (mass < 0) {
      break;
    }
    result += mass;
  }
  return result;
}

int main()
{
  std::ifstream input("01_input.txt"); 
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 0;
  }

  int total_fuel = 0, total_fuel_p2 = 0;
  std::string line;
  while (std::getline(input, line)) {
    int mass = atoi(line.c_str());
    total_fuel += fuel(mass);
    total_fuel_p2 += fuel_part2(mass);
  }

  std::cout << "Part #1: " << total_fuel << "\n";
  std::cout << "Part #2: " << total_fuel_p2 << "\n";
  input.close();
  return 0;
}
