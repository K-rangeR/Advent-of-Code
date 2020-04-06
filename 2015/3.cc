#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <vector>

struct Coordinate {
  int x;
  int y;

  Coordinate(int x, int y) : x{x}, y{y}
  {}

  bool operator==(const Coordinate& c) const
  {
    return (this->x == c.x) && (this->y == c.y);
  } };

class CoordinateHashFunc {
public:
  size_t operator()(const Coordinate& c) const
  {
    return c.x + c.y;
  }
};

void update_coord(const char dir, Coordinate& coord, const Coordinate& prev)
{
  if (dir == '^') {
    coord.y = prev.y + 1; 
    coord.x = prev.x;
  } else if (dir == 'v') {
    coord.y = prev.y - 1; 
    coord.x = prev.x;
  } else if (dir == '>') {
    coord.x = prev.x + 1; 
    coord.y = prev.y;
  } else {
    coord.x = prev.x - 1; 
    coord.y = prev.y;
  }
}

void part_one()
{
  std::ifstream input("3_input.txt");
  std::string line;
  input >> line;
  input.close();

  Coordinate curr_coord(0, 0);
  std::unordered_set<Coordinate, CoordinateHashFunc> coords;
  coords.insert(curr_coord);
  for (auto c : line) {
    Coordinate coord(0,0);
    update_coord(c, coord, curr_coord);
    coords.insert(coord);
    curr_coord = coord;
  }
  std::cout << coords.size() << "\n";
}

void part_two()
{ 
  std::ifstream input("3_input.txt");
  std::string line;
  input >> line;
  input.close();

  std::vector<Coordinate> santa{};
  santa.push_back(Coordinate(0, 0));

  std::vector<Coordinate> robo{};
  robo.push_back(Coordinate(0, 0));

  int dir_count = 1;
  for (auto d : line) {
    Coordinate coord(0, 0);
    if (dir_count % 2 == 1) {
      update_coord(d, coord, santa[santa.size()-1]);
      santa.push_back(coord);
    } else {
      update_coord(d, coord, robo[robo.size()-1]);
      robo.push_back(coord);
    }
    dir_count += 1;
  }

  std::vector<Coordinate> sr = santa;
  sr.insert(sr.end(), robo.begin(), robo.end());
  std::unordered_set<Coordinate, CoordinateHashFunc> coords(sr.begin(), sr.end());
  std::cout << coords.size() << "\n";
}

int main()
{
  part_one();
  part_two();
  return 0; 
}
