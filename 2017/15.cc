#include <iostream>

int main()
{
  constexpr unsigned long gen_a_factor = 16807;
  constexpr unsigned long gen_b_factor = 48271;
  constexpr unsigned long div_by = 2147483647;
  unsigned long gen_a_prev = 277, gen_b_prev = 349;
  constexpr unsigned long mask = (1 << 16) - 1;
  constexpr unsigned long to = 40000000;
  int answer = 0;

  for (int i = 0; i < to; ++i) {
    unsigned long next_a = (gen_a_prev * gen_a_factor) % div_by;
    unsigned long next_b = (gen_b_prev * gen_b_factor) % div_by;
    if ((next_a & mask) == (next_b & mask)) {
      answer++;
    }
    gen_a_prev = next_a;
    gen_b_prev = next_b;
  }

  std::cout << "Part #1: " << answer << "\n";
  return 0;
}
