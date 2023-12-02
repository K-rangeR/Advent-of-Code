import re

def find_first_digit(string):
    return string[re.search(r"\d", string).start()]    

def find_with_word(string):
    words = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    first, last = None, None
    for i in range(len(string)):
        if string[i].isdigit():
            first = string[i] if first == None else first
            last = string[i]
        else:
            for word in words.keys():
                if (i+len(word)) > len(string): continue
                token = string[i:i+len(word)]
                if token == word:
                    first = str(words[word]) if first == None else first
                    last = str(words[word])
                    break
    return first + last

def part2():
    with open('day01-input.txt', 'r') as f:
        answer = 0
        for line in f:
            answer += int(find_with_word(line.strip()))
        print(answer)

def part1():
    with open('day01-input.txt', 'r') as f:
        answer = 0
        for line in f:
            line = line.strip()
            first = find_first_digit(line)
            last = find_first_digit(line[::-1])
            answer += int((first + last))
        print(answer)

part1()
part2()
