#include <iostream>
#include <fstream>
#include <utility>
#include <unordered_map>

int main()
{
  std::ifstream input("11_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::unordered_map<std::string, std::pair<double,double>> directions {
    {"s", {0, -1}},
    {"n", {0, 1}},
    {"se", {0.5, -0.5}},
    {"sw", {-0.5, -0.5}},
    {"nw", {-0.5, 0.5}},
    {"ne", {0.5, 0.5}}
  };

  std::pair<double, double> pos {0, 0}; 
  std::string dir;
  double dist = 0.0;
  double max_dist = 0;
  while (std::getline(input, dir, ',')) {
    pos.first += directions[dir].first;  
    pos.second += directions[dir].second;
    double x = abs(pos.first);
    double y = abs(pos.second);
    dist = std::min(x, y) * 2.0 + std::max(0.0, x - y) * 2.0 + std::max(0.0, y - x);
    max_dist = std::max(max_dist, dist);
  }

  std::cout << (dist-1) << "\n"; 
  std::cout << max_dist << "\n";
  input.close();
  return 0;
}
