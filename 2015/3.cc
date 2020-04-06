#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>

struct Coordinate {
  int x;
  int y;

  Coordinate(int x, int y) : x{x}, y{y}
  {}

  bool operator==(const Coordinate& c) const
  {
    return (this->x == c.x) && (this->y == c.y);
  }
};

class CoordinateHashFunc {
public:
  size_t operator()(const Coordinate& c) const
  {
    return c.x + c.y;
  }
};

int main()
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
    if (c == '^') {         // north
      coord.y = curr_coord.y + 1; 
      coord.x = curr_coord.x;
    } else if (c == 'v') {  // south
      coord.y = curr_coord.y - 1; 
      coord.x = curr_coord.x;
    } else if (c == '>') {  // east
      coord.x = curr_coord.x + 1; 
      coord.y = curr_coord.y;
    } else {                // west
      coord.x = curr_coord.x - 1; 
      coord.y = curr_coord.y;
    }
    coords.insert(coord);
    curr_coord = coord;
  }
  std::cout << coords.size() << "\n";
  return 0; 
}
