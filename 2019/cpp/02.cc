#include <iostream>
#include "intcode.h"

void part1()
{
  IntCodeComputer computer {};
  if (computer.load_code("02_input.txt") < 0) {
    std::cerr << "Could not load code\n";
    return;
  }

  computer.run();
  std::cout << "Answer part 1: " << computer.value_at(0) << "\n";
}

void part2()
{
  for (int i = 0; i < 100; ++i) {
    for (int j = 0; j < 100; ++j) {
      IntCodeComputer computer {};
      computer.load_code("02_input.txt");
      computer.write_to(1, i);
      computer.write_to(2, j);
      computer.run();
      if (computer.value_at(0) == 19690720) {
        std::cout << "Answer part 2: " << (100 * i + j) << "\n"; 
        break;
      }
    }
  }
}

int main()
{
  part1();
  part2();

  return 0;
}
