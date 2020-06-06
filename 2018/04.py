#!/usr/bin/env python3
import re
import sys
import operator
from collections import defaultdict

# 1. sort input
# 2. find the guard who was asleep the most
# 3. find which minute they were asleep the most
# ID => [(sleep_at, wake_up_at), (...), (...)]

class Guard:
  def __init__(self, ID):
    self.id = ID
    self.total_sleep_time = 0
    self.sleep_intervals = []

  def add_to_total_sleep_time(self, increment):
    self.total_sleep_time += increment

  def get_total_sleep_time(self):
    return self.total_sleep_time

  def add_fall_a_sleep_time(self, minute):
    self.sleep_intervals.append([minute, 0])

  def add_wake_up_time(self, minute):
    self.sleep_intervals[-1][1] = minute

  def get_last_sleep_interval(self):
    sleep, wake_up = self.sleep_intervals[-1]
    return wake_up - sleep

  def get_most_common_slept_minute(self):
    tbl = defaultdict(lambda: 0, defaultdict(int))
    for (sleep, wake) in self.sleep_intervals:
      for i in range(sleep, wake+1):
        tbl[i] += 1
    return max(tbl.items(), key=operator.itemgetter(1))[0]


pattern = re.compile(r'\[(\d{4}\-\d{2}\-\d{2}) (\d{2}:\d{2})\].*')
get_time = re.compile(r'\d{2}:(\d{2})')

def main():
  timestamps = open('04_input.txt', 'r').read().strip().split('\n')
  timestamps.sort(key=sort_by_date_then_by_time)

  part_1(timestamps)

  
def sort_by_date_then_by_time(timestamp):
  m = pattern.match(timestamp)
  return (m.group(1), m.group(2))


def part_1(timestamps):
  guards = {}
  curr_guard_id = -1
  for timestamp in timestamps:
    tokens = timestamp.split(' ')
    if tokens[2] == 'Guard':
      guard_id = int(tokens[3][1:])
      if guard_id not in guards:
        guards[guard_id] = Guard(guard_id)
      curr_guard_id = guard_id
    elif tokens[2] == 'falls':
      asleep_time = int(get_time.match(tokens[1]).group(1))
      guards[curr_guard_id].add_fall_a_sleep_time(asleep_time)
    elif tokens[2] == 'wakes':
      guard = guards[curr_guard_id]
      wake_up_time = int(get_time.match(tokens[1]).group(1))
      guard.add_wake_up_time(wake_up_time)
      last_interval = guard.get_last_sleep_interval()    
      guard.add_to_total_sleep_time(last_interval)
    else:
      print('Unknown token to:', tokens[2])
      sys.exit(1)

  sleepiest_guard = None
  max_sleep = -1
  for (ID, guard) in guards.items():
    total_sleep_time = guard.get_total_sleep_time()
    if total_sleep_time > max_sleep:
      max_sleep = total_sleep_time
      sleepiest_guard = guard

  answer = sleepiest_guard.get_most_common_slept_minute() * sleepiest_guard.id
  print('Answer:', answer)


if __name__ == '__main__':
  main()
