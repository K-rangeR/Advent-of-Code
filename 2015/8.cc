#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <iterator>

int main()
{
  std::ifstream input("8_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

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
    //std::cout << res << "\n";
    total_str_len += res.length();
  }

  std::cout << "Code length: " << total_code_len << "\n";
  std::cout << "String length: " << total_str_len << "\n";

  int answer = total_code_len - total_str_len;
  std::cout << "Answer: " << answer << "\n";

  input.close();
  return 0;
}
