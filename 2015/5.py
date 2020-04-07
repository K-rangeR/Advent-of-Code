import re

def check_word(word):
  rule_one = re.search(r'(.).\1', word)
  rule_two = re.search(r'(..).*?\1', word)
  return rule_one and rule_two

count = 0
with open('5_input.txt', 'r') as data:
  for line in data:
    word = line.strip()
    if check_word(word):
      count += 1
      
print(count)
