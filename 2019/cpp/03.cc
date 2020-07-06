#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <cstdlib>


struct Point {
  Point(int xp, int yp) : x{xp}, y{yp} {}
  int dist_from_origin() const { return abs(x) + abs(y); }

  int x;
  int y;
};


class LineSegment {
public:
  LineSegment(Point one, Point two) : p1{one}, p2{two} {}
  Point intersect_at(const LineSegment& segment) const;
private:
  Point p1;
  Point p2;
};


class Wire {
public:
  Wire(int wire_id, std::vector<LineSegment> segments) 
    : id{wire_id}, line_segments{segments}
  {}
  int get_id() const { return id; }

private:
  const int id;
  std::vector<LineSegment> line_segments;
};


// Helper functions
Wire parse_input_line(std::string&);


int main()
{
  std::ifstream input("03_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::string line;
  while (std::getline(input, line)) {
    parse_input_line(line);
  }

  input.close();
  return 0;
}


Wire parse_input_line(std::string& line)
{
  std::vector<LineSegment> segments {};
  std::stringstream stream {line};
  std::string token;
  int x = 0, y = 0;

  while (std::getline(stream, token, ',')) {
    std::cout << token << "\n";
  }

  return Wire {0, segments}; 
}
