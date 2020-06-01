#!/usr/bin/env python3

def contains_anagram(words):
  for (i, word) in enumerate(words):
    for (j, word2) in enumerate(words):
      if (i == j) or (len(word) != len(word2)):
        continue
      word_sorted = ''.join(sorted(word))
      word2_sorted = ''.join(sorted(word2))
      if word_sorted == word2_sorted:
        return True
  return False


answer = 0
with open('04_input.txt', 'r') as f:
  for passphrase in f:
    passphrase = passphrase.strip().split()
    if not contains_anagram(passphrase):
      answer += 1
print("Answer:", answer)
