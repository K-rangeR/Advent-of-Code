#!/usr/bin/env python3
import re

with open('16_input.txt', 'r') as moves_input:
  moves = moves_input.read().strip().split(',')

places = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

spin_pattern = re.compile(r's(\d+)')
exchange_pattern = re.compile(r'x(\d+)/(\d+)')
partner_pattern = re.compile(r'p([a-p]+)/([a-p]+)')

for move in moves:
  match = spin_pattern.match(move)
  if match:
    n = int(match.group(1))
    last_n = places[-n:]
    places = last_n + places
    del places[-n:]

  match = exchange_pattern.match(move)
  if match:
    a, b = int(match.group(1)), int(match.group(2))
    places[a], places[b] = places[b], places[a]
    
  match = partner_pattern.match(move)
  if match:
    a, b = places.index(match.group(1)), places.index(match.group(2))
    places[a], places[b] = places[b], places[a]
    
print(''.join(places))
