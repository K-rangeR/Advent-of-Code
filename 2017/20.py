#!/usr/bin/env python3
import math


class Particle:
  def __init__(self, particle_id, position, velocity, acceleration):
    self.id = particle_id
    self.pos = position
    self.velocity = velocity
    self.acceleration = acceleration

  def update_position(self):
    for i in range(len(self.pos)):
      self.pos[i] += self.velocity[i] 

  def update_velocity(self):
    for i in range(len(self.velocity)):
      self.velocity[i] += self.acceleration[i]

  def manhattan_dist_from_origin(self):
    dist = 0
    for position in self.pos:
      dist += abs(position)
    return dist


def main():
  particles = []
  id_count = 0
  with open('20_input.txt', 'r') as particles_file:
    for particle in particles_file:
      parameters = particle.strip().split(' ')
      pos = parse_parameter(parameters[0])
      vel = parse_parameter(parameters[1])
      acc = parse_parameter(parameters[2])
      particles.append(Particle(id_count, pos, vel, acc))
      id_count += 1

  dists = [0 for i in range(len(particles))]
  for i in range(5000):
    for particle in particles:
      particle.update_velocity()
      particle.update_position()
      dists[particle.id] = particle.manhattan_dist_from_origin()

  print('Answer part #1:', dists.index(min(dists)))


def parse_parameter(parameter):
  open_brace, close_brace = parameter.index('<')+1, parameter.index('>')
  return list(map(int, parameter[open_brace:close_brace].split(',')))


if __name__ == '__main__':
  main()
