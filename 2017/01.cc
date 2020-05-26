#include <iostream>
#include <fstream>

int solve_captcha(const std::string& num)
{
  int sum = 0;
  for (int i = 0; i < num.length()-1; i++) {
    if (num[i] == num[i+1]) {
      sum += num[i] - '0';
    }
  }

  if (num[0] == num[num.length()-1]) {
      sum += num[0] - '0';
  }

  return sum;
}

int main()
{
  std::ifstream input("01_input.txt");  
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::string line;
  if (!std::getline(input, line)) {
    std::cerr << "Could not read input file\n";
    return 1;
  }

  int sum = solve_captcha(line);
  std::cout << "Answer: " << sum << "\n";

  input.close();
  return 0;
}
