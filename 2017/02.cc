#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

std::vector<int> split(std::string& s)
{
  size_t pos_start = 0, pos_end, delim_len = 1;
  int token;
  std::vector<int> tokens;

  while ((pos_end = s.find("\t", pos_start)) != std::string::npos) {
    token = std::stoi(s.substr(pos_start, pos_end - pos_start));
    pos_start = pos_end + delim_len;
    tokens.push_back(token);
  }

  tokens.push_back(std::stoi(s.substr(pos_start)));
  return tokens;
}

// Part 1
int calc_checksum(const std::vector<std::string>& table)
{
  int checksum = 0;
  for (auto row_str : table) {
    auto row = split(row_str);
    auto max = std::max_element(row.begin(), row.end());
    auto min = std::min_element(row.begin(), row.end());
    checksum += (*max - *min);
  }
  return checksum;
}

int main()
{
  std::ifstream input("02_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }
  
  std::vector<std::string> table {};
  std::string line;
  while (std::getline(input, line)) {
    table.push_back(line);  
  }

  int checksum = calc_checksum(table);
  std::cout << "Answer: " << checksum << "\n";

  input.close();
  return 0;
}
