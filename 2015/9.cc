#include <iostream>
#include <fstream>
#include <regex>
#include <set>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <tuple>
#include <limits>

using namespace std;

int get_dist(unordered_map<string, vector<tuple<string,int>>>& graph, 
             const string& from,
             const string& to)
{
  auto roads_out = graph[from];
  for (auto city : roads_out) {
    if (std::get<0>(city) == to) {
      return std::get<1>(city);
    }
  }
  std::cout << to << " NOT FOUND!!!\n";
  return 0; 
}

int main()
{
  std::ifstream input("9_input.txt");
  if (!input) {
    std::cout << "[!] Could not open input file\n";
    return 1;
  }

  unordered_map<string, vector<tuple<string, int>>> city_graph {};
  std::set<std::string> city_names {};
  std::regex rx("(\\w+) to (\\w+) = (\\d+)");
  std::string line;
  while (std::getline(input, line)) {
    std::smatch matches;
    std::regex_search(line, matches, rx);

    city_names.insert(matches[1].str());
    city_names.insert(matches[2].str());

    int dist = std::stoi(matches[3].str());
    auto road1 = std::make_tuple(matches[2].str(), dist);
    city_graph[matches[1].str()].push_back(road1);

    auto road2 = std::make_tuple(matches[1].str(), dist);
    city_graph[matches[2].str()].push_back(road2);
  }

  // Try all possible routes (input is small enough, only 7!)
  std::cout << "Number of cities: " << city_names.size() << "\n";
  int min_dist = std::numeric_limits<int>::max();
  std::vector<std::string> city_names_v(city_names.begin(), city_names.end());
  do {
    int curr_dist = 0;
    for (int i = 0; i < city_names_v.size()-1; ++i) {
      curr_dist += get_dist(city_graph, city_names_v[i], city_names_v[i+1]);
    }
    min_dist = std::min(min_dist, curr_dist);
  } while (std::next_permutation(city_names_v.begin(), city_names_v.end()));

  std::cout << "Shortest distance is: " << min_dist << "\n";

  input.close();
  return 0;
}
