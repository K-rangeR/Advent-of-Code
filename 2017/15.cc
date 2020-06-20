#include <iostream>

int main()
{
  constexpr uint64_t gen_a_factor = 16807;
  constexpr uint64_t gen_b_factor = 48271;
  constexpr uint64_t div_by = 2147483647;
  uint64_t gen_a_prev = 277, gen_b_prev = 349;
  constexpr uint64_t mask = (1 << 16) - 1;
  constexpr uint64_t to = 5000000;
  uint64_t next_a = 0, next_b = 0;
  int answer = 0;

  for (int i = 0; i < to; ++i) {
    do {
      next_a = (gen_a_prev * gen_a_factor) % div_by;
      gen_a_prev = next_a;
    } while (next_a % 4);

    do {
      next_b = (gen_b_prev * gen_b_factor) % div_by;
      gen_b_prev = next_b;
    } while (next_b % 8);

    if ((next_a & mask) == (next_b & mask)) {
      answer++;
    }
  }

  std::cout << answer << "\n";
  return 0;
}
