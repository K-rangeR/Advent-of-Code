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
  friend std::ostream& operator<<(std::ostream& out, const LineSegment& seg)
  {
    out << seg.p1.x << ", " << seg.p1.y << " - " << seg.p2.x << ", " << seg.p2.y;
    return out;
  }
private:
  Point p1;
  Point p2;
};


class Wire {
public:
  Wire(std::vector<LineSegment> segments) 
    : line_segments{segments}
  {}

  void print_line_segments() const
  {
    for (auto segment : line_segments) {
      std::cout << segment << "\n";
    }
  }

private:
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
    auto wire = parse_input_line(line);
    wire.print_line_segments();
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
    Point start {x, y};
    char dir = token[0];
    int displacement = atoi(token.c_str()+1);
    switch (dir) {
    case 'R':
      x += displacement;
      break;
    case 'L':
      x -= displacement;
      break;
    case 'D':
      y -= displacement;
      break;
    case 'U':
      y += displacement;
      break;
    }
    Point end {x, y};
    segments.push_back(LineSegment{start, end});
  }

  return Wire {segments}; 
}
