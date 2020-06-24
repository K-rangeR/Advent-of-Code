#!/usr/bin/env python3
import math
from collections import defaultdict


class Particle:
  def __init__(self, particle_id, position, velocity, acceleration):
    self.id = particle_id
    self.pos = position
    self.velocity = velocity
    self.acceleration = acceleration

  def update_position(self):
    self.pos[0] += self.velocity[0]
    self.pos[1] += self.velocity[1]
    self.pos[2] += self.velocity[2]

  def update_velocity(self):
    self.velocity[0] += self.acceleration[0]
    self.velocity[1] += self.acceleration[1]
    self.velocity[2] += self.acceleration[2]

  def manhattan_dist_from_origin(self):
    return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])


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
  
  #part1(particles)
  part2(particles)


def parse_parameter(parameter):
  open_brace, close_brace = parameter.index('<')+1, parameter.index('>')
  return list(map(int, parameter[open_brace:close_brace].split(',')))


def part1(particles):
  dists = [0 for i in range(len(particles))]
  for i in range(1000):
    for particle in particles:
      particle.update_velocity()
      particle.update_position()
      dists[particle.id] = particle.manhattan_dist_from_origin()

  print('Answer part #1:', dists.index(min(dists)))


def part2(particles):
  particles = {particle.id:particle for particle in particles}
  particles_at = defaultdict(list)
  for i in range(500):
    for particle in particles.values():
      particle.update_velocity()
      particle.update_position()
      position_tuple = tuple(particle.pos)
      particles_at[position_tuple].append(particle.id)

    for (pos, particle_ids) in particles_at.items():
      if len(particle_ids) > 1:
        for particle_id in particle_ids:
          del particles[particle_id]
      particles_at[pos].clear()

    print('len:', len(particles))
      

if __name__ == '__main__':
  main()
