#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <cstdlib>
#include <limits>


struct Point {
  Point(int xp, int yp) : x{xp}, y{yp} {}
  int dist_from_origin() const { return abs(x) + abs(y); }
  bool operator==(const Point& rhs) { return x == rhs.x && y == rhs.y; }

  int x;
  int y;
};


struct LineSegment {
  LineSegment(Point one, Point two) : p1{one}, p2{two} {}

  friend std::ostream& operator<<(std::ostream& out, const LineSegment& seg)
  {
    out << seg.p1.x << ", " << seg.p1.y << " - " << seg.p2.x << ", " << seg.p2.y;
    return out;
  }

  bool operator==(const LineSegment& rhs) { return p1 == rhs.p1 && p2 == rhs.p2; }

  Point p1;
  Point p2;
};


struct Wire {
  Wire(std::vector<LineSegment> segments) 
    : line_segments{segments}
  {}

  void print_line_segments() const
  {
    for (auto segment : line_segments) {
      std::cout << segment << "\n";
    }
  }

  std::vector<LineSegment> line_segments;
};


// Helper functions
Wire parse_input_line(std::string&);
int part1(const Wire& w1, const Wire& w2);
Point intersect_at(const LineSegment& one, const LineSegment& two);


int main()
{
  std::ifstream input("03_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::string line;
  std::getline(input, line);
  auto wire1 = parse_input_line(line);

  std::getline(input, line);
  auto wire2 = parse_input_line(line);

  std::cout << part1(wire1, wire2) << "\n";

  input.close();

  /*
  LineSegment one {Point{1,7}, Point{5,7}};
  LineSegment two {Point{4,5}, Point{4,9}};
  auto i = intersect_at(one, two);
  std::cout << i.x << ", " << i.y << "\n";
  */

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


int part1(const Wire& w1, const Wire& w2)
{
  int min_dist = std::numeric_limits<int>::max();
  for (auto l1 : w1.line_segments) { 
    for (auto l2 : w2.line_segments) {
      auto intersection = intersect_at(l1, l2);
      if (intersection.x != std::numeric_limits<int>::max()) {
        std::cout << intersection.x << ", " << intersection.y << "\n";
        int dist = intersection.dist_from_origin();
        std::cout << dist << "\n";
        min_dist = std::min(min_dist, dist);
      }
    }
  }
  return min_dist;
}


// one -> A = p1 B = p2
// two -> C = p1 D = p2
Point intersect_at(const LineSegment& one, const LineSegment& two)
{
  int a1 = one.p2.y - one.p1.y;
  int b1 = one.p1.x - one.p2.x;
  int c1 = a1 * (one.p1.x) + b1 * (one.p1.y);

  int a2 = two.p2.y - two.p1.y;
  int b2 = two.p1.x - two.p2.x;
  int c2 = a2 * (two.p1.x) + b2 * (two.p1.y);

  int determinant = a1 * b2 - a2 * b1;

  if (determinant == 0) {
    return Point{std::numeric_limits<int>::max(),std::numeric_limits<int>::max()};
  } else {
    int x = (b2 * c1 - b1 * c2) / determinant;
    int y = (a1 * c2 - a2 * c1) / determinant;
    return Point{x,y};
  }
}
