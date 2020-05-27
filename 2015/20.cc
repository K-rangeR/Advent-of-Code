#include <iostream>
#include <vector>
#include <numeric>
#include <math.h>

constexpr int input = 33100000;

std::vector<double> get_factors(int n)
{
  std::vector<double> factors {};
  double sqrt_n = sqrt(n);
  for (double i = 1.0; i <= sqrt_n; ++i) {
    if (n % (int)i == 0) {
      if (i <= 50) {
        factors.push_back(i);
      }
      if (i != sqrt_n) {
        if (i <= 50) {
          factors.push_back((n / i));
        }
      }
    }
  }
  return factors;
}

int main()
{
  for (int house = 1; house < std::numeric_limits<int>::max(); house++) {
    auto factors = get_factors(house);
    int total = 0;
    for (auto factor : factors) {
      total += (factor * 11);  // 10 for part 2
    }
    if (total >= input) {
      std::cout << "Answer: " << house << "\n";
      break;
    }
  }

  return 0;
}
