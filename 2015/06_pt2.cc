#include <iostream>
#include <fstream>
#include <string>
#include <vector>

constexpr int width = 1000;
constexpr int height = 1000;
std::vector<int> light_grid(width*height, 0);

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

void update_grid(int r1, int c1, 
                 int r2, int c2, 
                 std::function<void (int)> op)
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
                light_grid[index] += 2;
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
                if (flag) {
                  light_grid[index] += 1; 
                } else {
                  int val = light_grid[index];
                  light_grid[index] = (val > 0) ? --val : 0;
                }
              });
}

int get_total_brightness()
{
  int total = 0;
  for (int i = 0; i < width; ++i) {
    for (int j = 0; j < height; ++j) {
      int index = calc_index_in_light_grid(i, j);
      total += light_grid[index];
    }
  }
  return total;
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

  std::cout << get_total_brightness() << "\n";

  input.close();
  return 0;
}
