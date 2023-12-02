import re

def find_first_digit(string):
    return string[re.search(r"\d", string).start()]    

with open('day01-input.txt', 'r') as f:
    answer = 0
    for line in f:
        line = line.strip()
        first = find_first_digit(line)
        last = find_first_digit(line[::-1])
        answer += int((first + last))
    print(answer)
