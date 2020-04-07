#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

std::vector<char> vowels = {'a','e','i','o','u'};
std::vector<std::string> invalid = {"ab","cd","pq","xy"};

bool check_word(const std::string& word)
{
  int vowels_count = 0;
  bool double_char_found = false;

  for (int i = 0; i < word.length(); ++i) {
    // rule 1 check
    if (std::find(vowels.begin(), vowels.end(), word[i]) != vowels.end()) {
      vowels_count += 1;
    }

    if (i == word.length()-1) {
      continue;
    }

    std::string pair = word.substr(i, 2);

    // rule 2 check
    if (pair[0] == pair[1]) {
      double_char_found = true;
    }

    // rule 3 check
    if (std::find(invalid.begin(), invalid.end(), pair) != invalid.end()) {
      return false;
    }
  }
  return vowels_count >= 3 && double_char_found;
}

int main()
{
  std::ifstream input("5_input.txt");
  std::string line; 
  int nice_count = 0;
  while (std::getline(input, line)) {
    if (check_word(line)) {
      nice_count += 1;
    }
  }

  std::cout << nice_count << "\n";
  input.close();
  return 0;
}
