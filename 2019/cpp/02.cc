#include <iostream>
#include "intcode.h"

int main()
{
  IntCodeComputer computer {};
  if (computer.load_code("02_input.txt") < 0) {
    std::cerr << "Could not load code\n";
    return 1;
  }

  computer.run();
  std::cout << "Answer part 1: " << computer.value_at(0) << "\n";

  return 0;
}
