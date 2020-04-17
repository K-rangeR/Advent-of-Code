#include <iostream>
#include <string>

std::string get_next(const std::string& prev)
{
  std::string next = {""};
  char curr_digit = prev[0];
  int curr_digit_count = 1;
  for (auto it = prev.begin()+1; it != prev.end(); ++it) {
    if (*it != curr_digit) {
      next.append(std::to_string(curr_digit_count));
      next.push_back(curr_digit);
      curr_digit = *it;
      curr_digit_count = 1;
    } else {
      curr_digit_count++;
    }
  }
  next.append(std::to_string(curr_digit_count));
  next.push_back(curr_digit);
  return next;
}

std::string look_and_say_ith(int i, std::string& prev)
{
  if (i == 1) {
    return "1";
  }
  std::string curr {""};
  while (i > 0) {
    curr = get_next(prev);
    prev = curr;
    i--;
  }
  return curr;
}

int main()
{
  std::string input = "3113322113";
  std::string result = look_and_say_ith(50, input); // 40 part 1, 50 part 2
  std::cout << "Answer: " << result.length() << "\n";

  return 0;
}
