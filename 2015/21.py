import itertools
import math

weapons = [
  [8, 4, 0],
  [10, 5, 0],
  [25, 6, 0],
  [40, 7, 0],
  [74, 8, 0],
]

armors = [
  [0, 0, 0],
  [13,  0, 1],
  [31, 0, 2],
  [53, 0, 3],
  [75, 0, 4],
  [102, 0, 5],
]

rings = [
  [0, 0, 0],
  [0, 0, 0],
  [25, 1, 0],
  [50, 2, 0],
  [100, 3, 0],
  [20, 0, 1],
  [40, 0, 2],
  [80, 0, 3],
]

def fight(player_hp, player_damage, player_armor):
  enemy_hp, enemy_damage, enemy_armor = 103, 9, 2
  turn = 1
  while player_hp > 0 and enemy_hp > 0:
    if turn % 2 != 0:
      enemy_hp -= max(player_damage - enemy_armor, 1)
    else:
      player_hp -= max(enemy_damage - player_armor, 1)
    turn += 1
  return enemy_hp <= 0

COST_IDX = 0
DMG_IDX = 1
AMR_IDX = 2

# part 1
min_gold_spent = math.inf
for weapon in weapons:
  for armor in armors:
    for lh, rh in itertools.combinations(rings, 2):
      cost = weapon[COST_IDX] + armor[COST_IDX] + lh[COST_IDX] + rh[COST_IDX]
      damage = weapon[DMG_IDX] + lh[DMG_IDX] + rh[DMG_IDX]
      protection = armor[AMR_IDX] + lh[AMR_IDX] + rh[AMR_IDX]
      if fight(100, damage, protection):
        min_gold_spent = min(min_gold_spent, cost)

print('Min gold spent:', min_gold_spent)

# part 2
max_gold_spent = -1
for weapon in weapons:
  for armor in armors:
    for lh, rh in itertools.combinations(rings, 2):
      cost = weapon[COST_IDX] + armor[COST_IDX] + lh[COST_IDX] + rh[COST_IDX]
      damage = weapon[DMG_IDX] + lh[DMG_IDX] + rh[DMG_IDX]
      protection = armor[AMR_IDX] + lh[AMR_IDX] + rh[AMR_IDX]
      if not fight(100, damage, protection):
        max_gold_spent = max(max_gold_spent, cost)

print('Max gold spent:', max_gold_spent)
