#include <iostream>
#include <fstream>

int main()
{
  std::ifstream input("11_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  int x = 0, y = 0;
  std::string dir;
  while (std::getline(input, dir, ',')) {
    std::cout << dir << "\n";
    if (dir == "n") {
      y += 2;
    } else if (dir == "s") {
      y -= 2;
    } else if (dir == "ne") {
      y++;
      x++;
    } else if (dir == "sw") {
      x--;
      y--;
    } else if (dir == "nw") {
      y++;
      x--;
    } else if (dir == "se") {
      x++;
      y--;
    }
  }

  int answer = (abs(x) + abs(y)) / 2;
  std::cout << "Answer: " << answer << "\n";

  input.close();
  return 0;
}
