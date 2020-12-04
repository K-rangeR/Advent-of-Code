#include <iostream>
#include <fstream>
#include <unordered_map>

bool is_valid(std::unordered_map<std::string,bool>& fields)
{
  bool valid = true;
  for (auto key : fields) {
    if (key.second == false && key.first != "cid") {
      valid = false;
    }
    fields[key.first] = false; // reset
  }
  return valid;
}

void parse(const std::string& line, 
           std::unordered_map<std::string,bool>& fields)
{
  int i = 0;
  auto ptr = line.find(":");
  while (ptr != std::string::npos) {
    fields[line.substr(i, (ptr - i))] = true;

    ptr = line.find(" ", ptr);
    if (ptr == std::string::npos) {
      break;
    }
    i = ptr+1;
    ptr = line.find(":", ptr);
  }
}

int main()
{
  std::ifstream input("./input_04.txt");
  if (!input) {
    std::cerr << "Error opening the file\n";
    return 1;
  }

  std::unordered_map<std::string, bool> fields {
    {"byr",false}, {"iyr",false}, {"eyr",false},
    {"hgt",false}, {"hcl",false}, {"ecl",false},
    {"pid",false}, {"cid",false},
  };

  int valid_pwds = 0;
  std::string line;
  while (std::getline(input, line)) {
    if (line.length() == 0) {
      valid_pwds += is_valid(fields) ? 1 : 0;
    } else {
      parse(line, fields);
    }
  }
  valid_pwds += is_valid(fields) ? 1 : 0; // last line

  std::cout << "Answer: " << valid_pwds << "\n";

  input.close();
  return 0;
}
