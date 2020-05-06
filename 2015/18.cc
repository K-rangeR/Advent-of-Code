#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>


using std::vector;
using std::tuple;
using std::make_tuple;
using std::get;


const int STEPS = 100;
const int WIDTH = 100;


void print_lights(const vector<vector<char>>& lights) {
  for (auto i : lights) {
    for (auto j : i) {
      std::cout << j;
    }
    std::cout << "\n";
  }
  std::cout << "=============================\n";
}


int count_on_lights(const vector<vector<char>>& lights) {
  int on = 0;
  for (int i = 1; i < lights.size()-1; ++i) {
    for (int j = 1; j < lights[i].size()-1; ++j) {
      on += (lights[i][j] == '#') ? 1 : 0; 
    }
  }
  return on;
}

bool corner(int r, int c) {
  if (r == 1 && (c == 1 || c == WIDTH)) {
    return true;
  }
  if (r == WIDTH && (c == 1 || c == WIDTH)) {
    return true;
  }
  return false;
}


char change_light_to(int r, int c, vector<vector<char>>& lights) {
  if (corner(r, c)) {
    return '#'; // stuck on
  }

  int neighbors_on = 0;
  for (int i = r-1; i <= r+1; ++i) {
    for (int j = c-1; j <= c+1; ++j) {
      neighbors_on += (lights[i][j] == '#') ? 1 : 0; 
    }
  }

  char state = ' ';
  if (lights[r][c] == '#') {
    neighbors_on--;
    state = (neighbors_on == 2 || neighbors_on == 3) ? '#' : '.';
  } else {
    state = (neighbors_on == 3) ? '#' : '.';
  }

  return state;
}


void step(vector<vector<char>>& lights) {
  vector<tuple<int,int,char>> updates {};
  for (int i = 1; i < lights.size()-1; ++i) {
    for (int j = 1; j < lights[i].size()-1; ++j) {
      char state = change_light_to(i, j, lights);
      auto update = make_tuple(i, j, state);
      updates.push_back(update);
    }
  }

  // apply updates
  for (auto update : updates) {
    int r = get<0>(update), c = get<1>(update);
    char state = get<2>(update);
    lights[r][c] = state;
  }
}


int get_answer(vector<vector<char>>& lights) {
  for (int i = 0; i < STEPS; ++i) {
    step(lights);
  }
  return count_on_lights(lights);
}


int main() {
  std::ifstream input("18_input.txt");
  if (!input) {
    std::cout << "Could not open input file\n";
    return 1;
  }

  vector<vector<char>> lights {};
  std::string padding(WIDTH+2, '.');
  lights.push_back({padding.begin(), padding.end()});

  std::string line;
  while (std::getline(input, line)) {
    vector<char> line_vec {'.'};
    line_vec.insert(line_vec.end(), line.begin(), line.end());
    line_vec.push_back('.');
    lights.push_back(line_vec);
  }

  lights.push_back({padding.begin(), padding.end()});

  // Turn on the four corners (part #2)
  lights[1][1] = '#';
  lights[1][WIDTH] = '#';
  lights[WIDTH][1] = '#';
  lights[WIDTH][WIDTH] = '#';

  int answer = get_answer(lights);
  std::cout << "Answer: " << answer << "\n";

  input.close();
  return 0;
}
