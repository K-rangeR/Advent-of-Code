#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <regex>

bool is_document_valid(std::unordered_map<std::string,bool>& fields)
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

bool is_kv_pair_valid(const std::string& key, const std::string& value)
{
  if (key == "byr") {
    int byr = std::stoi(value);
    return byr >= 1920 && byr <= 2002;
  } else if (key == "iyr") {
    int iyr = std::stoi(value);
    return iyr >= 2010 && iyr <= 2020;
  } else if (key == "eyr") {
    int eyr = std::stoi(value);
    return eyr >= 2020 && eyr <= 2030;
  } else if (key == "hgt") {
    auto ptr = value.find("c");
    if (ptr == std::string::npos) {
      ptr = value.find("i");
      if (ptr == std::string::npos) {
        return false;
      }
    }
    int n = std::stoi(value.substr(0, ptr));
    if (value.at(ptr) == 'c') {
      return n >= 150 && n <= 193;
    } else {
      return n >= 59 && n <= 76;
    }
  } else if (key == "hcl") {
    return std::regex_match(value, std::regex("#[0-9a-f]{6}"));
  } else if (key == "ecl") {
    return value == "blu" || value == "gry" || value == "brn" ||
           value == "grn" || value == "hzl" || value == "oth" || value == "amb";
  } else if (key == "pid") {
    return std::regex_match(value, std::regex("[0-9]{9}"));
  } else if (key == "cid") {
    return true;
  }

  return false;
}

void parse(const std::string& line, 
           std::unordered_map<std::string,bool>& fields)
{
  int i = 0;
  auto ptr = line.find(":");
  std::string key, value;
  while (ptr != std::string::npos) {
    key = line.substr(i, (ptr - i));

    i = ptr+1;
    ptr = line.find(" ", ptr);
    if (ptr != std::string::npos) {
      value = line.substr(i, (ptr - i));
    } else { // last key value pair
      value = line.substr(i, std::string::npos);
    }

    fields[key] = is_kv_pair_valid(key, value);

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
      valid_pwds += is_document_valid(fields) ? 1 : 0;
    } else {
      parse(line, fields);
    }
  }
  valid_pwds += is_document_valid(fields) ? 1 : 0; // last line

  std::cout << "Answer: " << valid_pwds << "\n";

  input.close();
  return 0;
}
