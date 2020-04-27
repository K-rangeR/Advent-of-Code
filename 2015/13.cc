#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
#include <set>
#include <algorithm>
#include <unordered_map>
#include <numeric>

using std::string;
using std::vector;
using std::set;
using std::unordered_map;
using std::stoi;

int solve(vector<string>& people, 
          unordered_map<string, unordered_map<string, int>> arrangements)
{
  int max_happiness = std::numeric_limits<int>::min();
  int len = people.size();

  do {
    int curr_happiness = 0;
    for (int i = 0; i < len; ++i) {
      auto person1_name = people[i]; 
      auto person2_name = people[(i+1) % len];
      int hu1 = arrangements[person1_name][person2_name];
      int hu2 = arrangements[person2_name][person1_name];
      curr_happiness += hu1 + hu2;
    }
    max_happiness = std::max(max_happiness, curr_happiness);
  } while (std::next_permutation(people.begin(), people.end()));

  return max_happiness;
}

int main()
{
  std::ifstream input("13_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::regex input_pattern(
    "^(\\w+) would (\\w+) (\\d+) happiness units by sitting next to (\\w+)\\."
  );

  set<string> people {};
  unordered_map<string, unordered_map<string, int>> arrangements {};
  string line;
  while (std::getline(input, line)) {
    std::smatch args;
    std::regex_match(line, args, input_pattern);
    people.insert(args[1]);
    arrangements[args[1]][args[4]] = (args[2] == "gain") ? stoi(args[3])
                                                         : -1 * stoi(args[3]);
  }

  vector<string> people_v {people.begin(), people.end()};
  int answer = solve(people_v, arrangements);
  std::cout << "Answer: " << answer << "\n";

  input.close();
  return 0;
}
