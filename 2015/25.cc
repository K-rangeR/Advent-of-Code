#include <iostream>

uint64_t calc_next_code(uint64_t prev_code)
{
  return (prev_code * 252533) % 33554393;
}

int main()
{
  int answer_row = 2981, answer_col = 3075;
  int row = 1, col = 1;
  uint64_t curr_code = 20151125;
  
  while (true) {
    if (row == 1) {
      row = col + 1;
      col = 1;
    } else {
      row -= 1;
      col += 1;
    }
    uint64_t next_code = calc_next_code(curr_code);
    if (row == answer_row && col == answer_col) {
      std::cout << "Answer part 1: " << next_code << "\n";
      break;
    }
    curr_code = next_code;
  }

  return 0;
}
