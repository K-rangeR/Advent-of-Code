import sys
import re


def rotate_column(screen, column, by):
  pass


def rotate_row(screen, row, by):
  pass


def fill_rect(screen, x, y):
  for i in range(x):
    for j in range(y):
      screen[i][j] = '#'


def print_screen(screen):
  for i in range(6):
    for j in range(50):
      print(screen[i][j], end='')
    print()
       

def count_lights_on(screen):
  on = 0
  for i in range(6):
    for j in range(50):
      if screen[i][j] == '#':
        on += 1
  return on


rect = re.compile(r'rect (\d+)x(\d+)')
row = re.compile(r'rotate row y=(\d+) by (\d+)')
column = re.compile(r'rotate column x=(\d+) by (\d+)')

screen = [['.' for i in range(50)] for j in range(6)]

'''
with open('08_input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    match = rect.match(line)
    if match:
      fill_rect(screen, match.group(1), match.group(2))
    
    match = row.match(line)
    if match:
      rotate_row(screen, match.group(1), match.group(2))      

    match = column.match(line)
    if match:
      rotate_column(screen, match.group(1), match.group(2))      
'''

fill_rect(screen, 3, 3)
print_screen(screen)
on = count_lights_on(screen)
print('Answer:', on)
