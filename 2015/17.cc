#include <iostream>
#include <vector>
#include <fstream>

int get_answer(int at, int liters_left, const std::vector<int>& data)
{
  if (at == data.size()) {
    return 0;
  }

  int curr_count = 0;
  if (data[at] == liters_left) {
    curr_count = 1;
  } else if (data[at] < liters_left) {
    curr_count = get_answer(at+1, liters_left - data[at], data);
  }

  return curr_count + get_answer(at+1, liters_left, data);
}

int main()
{
  std::ifstream input("17_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  std::vector<int> data {};
  std::string line;
  while (std::getline(input, line)) {
    data.push_back(std::stoi(line));
  }

  int answer = get_answer(0, 150, data);
  std::cout << "Answer: " << answer << "\n";

  input.close();
  return 0;
}
