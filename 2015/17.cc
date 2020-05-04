#include <iostream>
#include <vector>
#include <fstream>

int get_answer(int at, 
               int liters_left, 
               int containers,
               const std::vector<int>& data,
               std::vector<int>& container_count)
{
  if (at == data.size()) {
    return 0;
  }

  int curr_count = 0;
  if (data[at] == liters_left) {
    container_count.push_back(containers+1);
    curr_count = 1;
  } else if (data[at] < liters_left) {
    curr_count = get_answer(at+1, liters_left-data[at], containers+1, 
                            data, container_count);
  }

  return curr_count + get_answer(at+1, liters_left, containers, 
                                 data, container_count);
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

  std::vector<int> container_count {};
  int answer = get_answer(0, 150, 0, data, container_count);
  std::cout << "Part #1 answer: " << answer << "\n";

  auto min = std::min_element(container_count.begin(), container_count.end());
  int answer2 = 0;
  for (auto i : container_count) {
    if (i == *min) {
      answer2++;
    }
  }
  std::cout << "Part #2 answer: " << answer2 << "\n";

  input.close();
  return 0;
}
