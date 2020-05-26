import sys
import re


def rotate_column(screen, column, by):
  for i in range(6):
    for j in range(i + by):
      j = j % 6
      screen[i][column], screen[j][column] = screen[j][column], screen[i][column]
    

def rotate_row(screen, row, by):
  print(row, by)
  for i in range(50):
    for j in range(i + by):
      j = j % 50 
      screen[row][i], screen[row][j] = screen[row][j], screen[row][i]


def fill_rect(screen, x, y):
  for i in range(y):
    for j in range(x):
      screen[i][j] = '#'


def print_screen(screen, rows, columns):
  for i in range(rows):
    for j in range(columns):
      print(screen[i][j], end='')
    print()
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
      fill_rect(screen, int(match.group(1)), int(match.group(2)))
    
    match = row.match(line)
    if match:
      rotate_row(screen, int(match.group(1)), int(match.group(2)))

    match = column.match(line)
    if match:
      rotate_column(screen, int(match.group(1)), int(match.group(2)))
'''

fill_rect(screen, 1, 1)
print_screen(screen, 6, 50)
rotate_row(screen, 0, 10)
print_screen(screen, 6, 50)

'''
on = count_lights_on(screen)
print('Answer:', on)
'''
