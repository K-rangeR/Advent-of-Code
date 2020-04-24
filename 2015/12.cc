#include <iostream>
#include <fstream>
#include <regex>
#include <cctype>

int main()
{
  std::ifstream input("12_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  std::string line;
  std::getline(input, line);

  int sum = 0;
  std::string curr_number {""};
  for (auto c : line) {
    if (isdigit(c) || c == '-') {
      curr_number += c; 
    } else {
      if (!curr_number.empty()) {
        sum += std::stoi(curr_number);
        curr_number.clear();
      }
    }
  }

  std::cout << "Answer: " << sum << "\n";

  input.close();
  return 0;
}
