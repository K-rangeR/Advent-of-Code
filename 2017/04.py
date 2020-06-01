answer = 0
with open('04_input.txt', 'r') as f:
  for passphrase in f:
    passphrase = passphrase.strip().split()
    if len(passphrase) == len(set(passphrase)):
      print(passphrase)
      answer += 1
print("Answer:", answer)
