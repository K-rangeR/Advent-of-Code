#include <iostream>

bool meets_rule_one(const std::string& pwd)
{
  int sublen = 1;
  char prev = pwd[0];
  for (int i = 1; i < pwd.size(); ++i) {
    if (pwd[i]-1 == prev) {
      sublen++;
      if (sublen == 3) {
        return true;
      }
    } else {
      sublen = 1;
    }
    prev = pwd[i];
  }
  return false;
}

bool meets_rule_two(const std::string& pwd)
{
  for (auto c : pwd) {
    if (c == 'i' || c == 'o' || c == 'l') {
      return false;
    }
  }
  return true;
}

bool meets_rule_three(const std::string& pwd)
{
  bool already_found_pair = false;
  char letter_of_pair = ' ';
  for (int i = 0; i < pwd.size()-1; ++i) {
    if (pwd[i] == pwd[i+1]) {
      if (already_found_pair && pwd[i] != letter_of_pair) {
        return true;
      } else if (!already_found_pair) {
        already_found_pair = true; 
        letter_of_pair = pwd[i];
      }
    }
  }
  return false;
}

std::string get_next_pwd(std::string pwd)
{
  int i = pwd.size()-1;
  if (pwd.back() == 'z') {
    while (i >= 0 && pwd[i] == 'z') {
      pwd[i] = 'a'; 
      i--;
    }
  }
  pwd[i] = pwd[i]+1;
  return pwd;
}

int main()
{
  std::string curr_pwd = "hepxxzaa";
  while (curr_pwd != "zzzzzzzz") {
    bool rule1 = meets_rule_one(curr_pwd);
    bool rule2 = meets_rule_two(curr_pwd);
    bool rule3 = meets_rule_three(curr_pwd);
    if (rule1 && rule2 && rule3) {
      std::cout << "Next valid password is: " << curr_pwd << "\n";
      break;
    }
    curr_pwd = get_next_pwd(curr_pwd);
  }
    
  return 0;
}
