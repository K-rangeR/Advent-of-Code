#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <iterator>

int get_real_len(const std::string& str)
{
  int len = 0;
  for (auto it = str.begin(); it < str.end(); it++) {
    if (*it == '\"') {
      std::cout << "found quote: " << *it << "\n";
      len += 2;
    } else if (*it == '\\') {
      std::cout << "found slash: " << *it << "\n";
      len += 2;
    } else {
      len += 1;
    }
  }
  return len + 2; // add in the surrounding double quotes
}

void part_2(std::ifstream& input)
{
  int total_code_len = 0, real_string_len = 0;
  std::string line;
  while (std::getline(input, line)) {
    total_code_len += line.length();
    real_string_len += get_real_len(line);
  }

  std::cout << "Code length: " << total_code_len << "\n";
  std::cout << "Real string length: " << real_string_len << "\n";

  int answer = real_string_len - total_code_len;
  std::cout << "[2] Answer: " << answer << "\n";
}

void part_1(std::ifstream& input)
{
  std::regex e("\\\\(x(\\d|[a-f])(\\d|[a-f])|\\\\|\")");

  int total_code_len = 0, total_str_len = 0;
  std::string line;
  while (std::getline(input, line)) {
    total_code_len += line.length();
    std::string res;
    std::regex_replace(std::back_inserter(res), 
                       line.begin()+1, 
                       line.end()-1,
                       e, "A");
    total_str_len += res.length();
  }

  std::cout << "Code length: " << total_code_len << "\n";
  std::cout << "String length: " << total_str_len << "\n";

  int answer = total_code_len - total_str_len;
  std::cout << "[1] Answer: " << answer << "\n";
}

int main()
{
  std::ifstream input("8_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  part_1(input);
  part_2(input);

  input.close();
  return 0;
}
