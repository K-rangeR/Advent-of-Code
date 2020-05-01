#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
#include <numeric>

int calc_score(int a, int b, int c, int d, const std::vector<int>& data)
{
  int score = 0;
  score += (a * data[0]);
  score += (b * data[1]);
  score += (c * data[2]);
  score += (d * data[3]);
  return (score >= 0) ? score : 0;
}

int main()
{
  std::ifstream input("15_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::regex pattern(
    "(\\w+): \\w+ (-?\\d+), \\w+ (-?\\d+), \\w+ (-?\\d+), \\w+ (-?\\d+), \\w+ (-?\\d+)"
  );

  std::vector<int> capacities {};
  std::vector<int> durabilities {};
  std::vector<int> flavors {};
  std::vector<int> textures {};
  std::vector<int> calories {};

  std::string line;
  while (std::getline(input, line)) {
    std::smatch tokens;
    std::regex_match(line, tokens, pattern);

    capacities.push_back(std::stoi(tokens[2]));
    durabilities.push_back(std::stoi(tokens[3]));
    flavors.push_back(std::stoi(tokens[4]));
    textures.push_back(std::stoi(tokens[5]));
    calories.push_back(std::stoi(tokens[6]));
  }

  std::vector<int> results {4};
  int curr_max_score = std::numeric_limits<int>::min();
  for (int a = 0; a < 100; ++a) {
    for (int b = 0; b < 100 - a; ++b) {
      for (int c = 0; c < 100 - a - b; ++c) {
        int d = 100 - a - b - c;
        results.push_back(calc_score(a,b,c,d,capacities));
        results.push_back(calc_score(a,b,c,d,durabilities));
        results.push_back(calc_score(a,b,c,d,flavors));
        results.push_back(calc_score(a,b,c,d,textures));

        int curr_score = 1;
        for (int res : results) { curr_score *= res; }
        curr_max_score = std::max(curr_score, curr_max_score);

        results.clear();
      }
    }
  }
  
  std::cout << "Answer: " << curr_max_score << "\n";

  input.close();
  return 0;
}
