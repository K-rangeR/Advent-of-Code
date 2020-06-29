#!/urs/bin/env python3

class Component:
  def __init__(self, a, b): 
    self.a = a
    self.b = b
    self.visited = False


max_strength = 0


def main():
  global max_strength
  components = read_data_file()
  get_max_strength(0, 0, components)
  print('Answer part #1:', max_strength)


def read_data_file():
  components = []
  with open('24_input.txt', 'r') as data_file:
    for line in data_file:
      tokens = list(map(int, line.strip().split('/')))
      components.append(Component(tokens[0], tokens[1]))
  return components


def get_max_strength(port, strength, components):
  global max_strength
  max_strength = max(strength, max_strength)
  for c in components:
    if not c.visited and (c.a == port or c.b == port):
      c.visited = True
      new_port = c.b if c.a == port else c.a
      get_max_strength(new_port, strength+c.a+c.b, components)
      c.visited = False
  

if __name__ == '__main__':
  main()
