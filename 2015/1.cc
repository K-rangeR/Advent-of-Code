#include <iostream>
#include <fstream>
#include <string>

int main()
{
  std::string line;
  std::ifstream file("1_input.txt");
  file >> line;
  file.close();
  
  int floor = 0, line_cnt = 1;
  for (auto c : line) {
    if (c == '(') {
      floor++;
    } else {
      floor--;
    }

    if (floor == -1) {
      std::cout << line_cnt << "\n";
    }

    line_cnt++;
  }
  
  std::cout << floor << "\n";
  return 0;
}
