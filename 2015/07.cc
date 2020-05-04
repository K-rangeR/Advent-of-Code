// TODO: not complete
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <regex>

int main()
{
  std::ifstream input("7_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  std::regex assign("(\\w+) -> (\\w+)");
  std::regex binary("(\\w+) (AND|OR|LSHIFT|RSHIFT) (\\w+) -> (\\w+)");
  std::regex not_pattern("NOT (\\w+) -> (\\w+)");
  
  std::string line;
  while (std::getline(input, line)) {
    std::cout << line << "\n";
  }

  input.close();
  return 0;
}
