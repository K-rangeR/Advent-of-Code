#include <fstream>
#include <iostream>
#include <regex>
#include <vector>
#include <algorithm>

using std::stoi;

const int TOTAL_FLY_TIME = 2503;

enum class State {flying, resting};

struct Reindeer {
  std::string name;
  int speed;
  int fly_time;
  int rest_time;
  int fly_at;
  int rest_at;
  int dist;
  int points;
  State state;

  Reindeer(std::string name, int speed_km, int fly_time, int rest_time)
    : name{name}, speed{speed_km}, fly_time{fly_time}, rest_time{rest_time},
      fly_at{1}, rest_at{1}, dist{0}, points{0}, state{State::flying}
  {}

  bool operator<(Reindeer const& rhs) const { return dist < rhs.dist; }
};

bool dist_cmp(const Reindeer& lhs, const Reindeer& rhs)
{
  return lhs.dist < rhs.dist;
}

bool points_cmp(const Reindeer& lhs, const Reindeer& rhs)
{
  return lhs.points < rhs.points;
}

int main()
{
  std::ifstream input("14_input.txt");
  if (!input) {
    std::cerr << "Could not open input file\n";
    return 1;
  }

  std::regex line_pattern(
    "(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds\\."
  );

  std::vector<Reindeer> reindeer {};
  std::string line;
  while (std::getline(input, line)) {
    std::smatch args;
    std::regex_match(line, args, line_pattern);
    Reindeer deer(args[1], stoi(args[2]), stoi(args[3]), stoi(args[4]));
    reindeer.push_back(deer);
  }

  for (int sec = 1; sec <= TOTAL_FLY_TIME; ++sec) {
    std::for_each(reindeer.begin(), reindeer.end(), [&](Reindeer& r) {
      // stop flying and rest
      if (sec == (r.fly_at + r.fly_time)) {
        r.state = State::resting; 
        r.rest_at = sec;
      }
      // stop resing and fly
      if (sec == (r.rest_at + r.rest_time)) {
        r.state = State::flying; 
        r.fly_at = sec;
      }
      // update dist
      if (r.state == State::flying) {
        r.dist += r.speed;
      }
    });

    // award points to leader(s)
    auto current_winner_dist = std::max_element(reindeer.begin(), 
                                                reindeer.end(),
                                                dist_cmp)->dist;

    std::for_each(reindeer.begin(), reindeer.end(), [&](Reindeer& r) {
      if (r.dist == current_winner_dist) {
        r.points += 1; 
      }
    });
  }

  auto deer = std::max_element(reindeer.begin(), 
                               reindeer.end(), 
                               points_cmp);
  std::cout << deer->name << ": " << deer->points << "\n";

  input.close();
  return 0;
}
