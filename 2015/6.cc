#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>

constexpr int width = 1000;
constexpr int height = 1000;
std::bitset<width*height> light_grid {}; // all lights are off at the start

std::vector<std::string> split(const std::string& s, const std::string& del)
{
  size_t pos_start = 0, pos_end, delim_len = 1;
  std::string token;
  std::vector<std::string> tokens;

  while ((pos_end = s.find(del, pos_start)) != std::string::npos) {
    token = s.substr(pos_start, pos_end - pos_start);
    pos_start = pos_end + delim_len;
    tokens.push_back(token);
  }

  tokens.push_back(s.substr(pos_start));
  return tokens; 
}

inline int calc_index_in_light_grid(int row, int column)
{
  return row * width + column;
}

void update_grid(int r1, int c1, int r2, int c2, std::function<void (int)> op)
{
  for (int i = r1; i <= r2; ++i) {
    for (int j = c1; j <= c2; ++j) {
      op(calc_index_in_light_grid(i, j));
    }
  }
}

void handle_toggle(const std::vector<std::string>& tokens)
{
  std::vector<std::string> cell1 = split(tokens[1], ",");
  std::vector<std::string> cell2 = split(tokens[3], ",");
  update_grid(std::stoi(cell1[0]),
              std::stoi(cell1[1]),
              std::stoi(cell2[0]),
              std::stoi(cell2[1]),
              [](int index) { 
                light_grid[index] = light_grid[index] ^ 1;
              });
}

void handle_on_off(const std::vector<std::string>& tokens, bool flag)
{
  std::vector<std::string> cell1 = split(tokens[2], ",");
  std::vector<std::string> cell2 = split(tokens[4], ",");
  update_grid(std::stoi(cell1[0]),
              std::stoi(cell1[1]),
              std::stoi(cell2[0]),
              std::stoi(cell2[1]),
              [&](int index) {
                light_grid[index] = flag;
              });
}

int main()
{
  std::ifstream input("6_input.txt");
  if (!input) {
    std::cout << "Could not open file\n"; 
    return 1;
  }

  std::string line;
  while (std::getline(input, line)) {
    std::vector<std::string> tokens = split(line, " ");
    if (tokens[0] == "toggle") {
      handle_toggle(tokens);
    } else if (tokens[0] == "turn") {
      bool flag = (tokens[1] == "on") ? 1 : 0;
      handle_on_off(tokens, flag);
    } else {
      std::cout << "Unknown operation: " << tokens[0] << "\n";
      break;
    }
  }

  std::cout << light_grid.count() << "\n";

  input.close();
  return 0;
}
