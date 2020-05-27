#include <iostream>
#include <vector>
#include <numeric>
#include <math.h>

std::vector<double> get_factors(int n)
{
  std::vector<double> factors {};
  double sqrt_n = sqrt(n);
  for (double i = 1.0; i < sqrt_n; ++i) {
    if (n % (int)i == 0) {
      factors.push_back(i);      
      if (i != sqrt_n) {
        factors.push_back((n / i));
      }
    }
  }
  return factors;
}

int main()
{
  constexpr int input = 33100000;
  for (int house = 1; house < std::numeric_limits<int>::max(); house++) {
    auto factors = get_factors(house);
    int total = 0;
    for (auto factor : factors) {
      total += (factor * 10); 
    }
    if (total >= input) {
      std::cout << "Answer: " << house << "\n";
      break;
    }
  }
  
  return 0;
}
