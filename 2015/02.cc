#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

const int length = 0;
const int width = 1;
const int height = 2;

std::vector<int> split(std::string& s)
{
  size_t pos_start = 0, pos_end, delim_len = 1;
  int token;
  std::vector<int> tokens;
  
  while ((pos_end = s.find("x", pos_start)) != std::string::npos) {
    token = std::stoi(s.substr(pos_start, pos_end - pos_start));
    pos_start = pos_end + delim_len;
    tokens.push_back(token);
  }

  tokens.push_back(std::stoi(s.substr(pos_start)));
  return tokens;
}

int main()
{
  int total = 0;
  std::string line;
  std::ifstream infile("2_input.txt"); 
  while (std::getline(infile, line)) {
    std::vector<int> input = split(line);
    int l = input[length];
    int w = input[width];
    int h = input[height];
    
    int bow_len = l * w * h;

    auto max = std::max_element(input.begin(), input.end());
    input.erase(
      std::remove_if(
        input.begin(), input.end(), [&](int i){ return i == *max; }
      ),
      input.end()
    );
    int wrapper_len = (input[0] * 2) + (input[1] * 2);

    total += wrapper_len + bow_len;
  }

  std::cout << total << "\n";
  infile.close();
  return 0;
}
