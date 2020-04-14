// TODO: not complete!!!
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main()
{
  std::ifstream input("7_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }
  
  std::string line;
  while (std::getline(input, line)) {
    std::cout << line << "\n";
  }

  input.close();
  return 0;
}
