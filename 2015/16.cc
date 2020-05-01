#include <iostream>
#include <vector>
#include <fstream>
#include <regex>
#include <unordered_map>

int main()
{
  std::ifstream input {"16_input.txt"};
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  std::regex pattern {
    "Sue \\d+: (\\w+): (\\d+), (\\w+): (\\d+), (\\w+): (\\d+)"
  };

  std::unordered_map<std::string, int> target_sue {
    {"children", 3},
    {"cats", 7},
    {"samoyeds", 2},
    {"pomeranians", 3},
    {"akitas", 0},
    {"vizslas", 0},
    {"goldfish", 5},
    {"trees", 3},
    {"cars", 2},
    {"perfumes", 1}
  };

  std::vector<int> sue_correct_count {};
  std::string line;
  while (std::getline(input, line)) {
    std::smatch tokens;
    std::regex_match(line, tokens, pattern);
    int matching_count = 0;
    for (auto token = tokens.begin()+1; token != tokens.end(); token+=2) {
      auto compound = target_sue.find(*token);
      if (compound != target_sue.end()) {
        int val = std::stoi(*(token+1));
        if (*token == "cats" || *token == "trees") {
          matching_count += (val > compound->second) ? 1 : 0; 
        } else if (*token == "pomeranians" || *token == "goldfish") {
          matching_count += (val < compound->second) ? 1 : 0; 
        } else {
          matching_count += (compound->second == val) ? 1 : 0;  
        }
      } else {
        std::cout << "Could not find that compound: " << *token << "\n";
      }
    }
    sue_correct_count.push_back(matching_count);
  }

  int idx = 0;
  int max = std::numeric_limits<int>::min();
  for (int i = 0; i < sue_correct_count.size(); ++i) {
    if (sue_correct_count[i] > max) {
      max = sue_correct_count[i]; 
      idx = i;
    }
  }
  
  std::cout << "Index of max: " << idx << ", Max: " << max << "\n"; 

  input.close();
  return 0;
}
