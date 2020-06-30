#!/urs/bin/env python3
from collections import defaultdict


def component_table(pairs):
  ctable = defaultdict(set)
  for pair in pairs:
    ctable[pair[0]].add(pair)
    ctable[pair[1]].add(pair)
  return ctable


def other_port(component, port):
  return (component[1] if component[0] == port else component[0])


# Adapted Peter Norvigs solution for part 2
def strongest_chain(ctable):
  chain = set()
  port = 0
  strength = 0
  paths = [] # (len, strength)
  def recurse(best_strength):
    nonlocal chain, port, strength, paths
    for c in ctable[port] - chain:
      chain.add(c)
      port = other_port(c, port)
      strength += sum(c)
      paths.append((len(chain), strength))
      best_strength = max(strength, recurse(best_strength))
      strength -= sum(c)
      chain.remove(c)
      port = other_port(c, port)
    return best_strength
  res = recurse(0)
  print(max(paths))
  return res


pairs = []
with open('24_input.txt', 'r') as components_file:
  for line in components_file:
    tokens = list(map(int, line.strip().split('/')))
    pairs.append((tokens[0], tokens[1]))

ctable = component_table(pairs)
print(strongest_chain(ctable))
