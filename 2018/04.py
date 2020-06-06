#!/usr/bin/env python3
import re
import sys
import operator
from collections import defaultdict


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
    if len(self.sleep_intervals) == 0:
      return (-1, -1)

    tbl = defaultdict(lambda: 0, defaultdict(int))
    for (sleep, wake) in self.sleep_intervals:
      for i in range(sleep, wake+1):
        tbl[i] += 1
    return max(tbl.items(), key=operator.itemgetter(1))


pattern = re.compile(r'\[(\d{4}\-\d{2}\-\d{2}) (\d{2}:\d{2})\].*')
get_time = re.compile(r'\d{2}:(\d{2})')


def main():
  timestamps = open('04_input.txt', 'r').read().strip().split('\n')
  timestamps.sort(key=sort_by_date_then_by_time)

  #part_1(timestamps)
  part_2(timestamps)

  
def sort_by_date_then_by_time(timestamp):
  m = pattern.match(timestamp)
  return (m.group(1), m.group(2))


def part_1(timestamps):
  guards = process_input(timestamps)
  sleepiest_guard = None
  max_sleep = -1
  for (ID, guard) in guards.items():
    total_sleep_time = guard.get_total_sleep_time()
    if total_sleep_time > max_sleep:
      max_sleep = total_sleep_time
      sleepiest_guard = guard

  answer = sleepiest_guard.get_most_common_slept_minute()[0] * sleepiest_guard.id
  print('Answer:', answer)


def part_2(timestamps):
  guards = process_input(timestamps)
  guard_id = -1
  minute_count = -1
  minute = -1
  for guard in guards.values():
    most_freq_min, count = guard.get_most_common_slept_minute()
    if count > minute_count:
      minute_count = count
      guard_id = guard.id
      minute = most_freq_min
  print('Answer:', (guard_id * minute))


def process_input(timestamps):
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
  return guards


if __name__ == '__main__':
  main()
