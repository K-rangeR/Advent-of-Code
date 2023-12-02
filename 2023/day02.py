import re

# only need to track the max count
def parse_input_line(line):
    game_id = int(re.match(r"Game (\d+)", line).group(1))
    sets = line.split(":")[1:][0].split(";")
    map = {}
    for s in sets:
        draws = s.split(",")
        for draw in draws:
            count, color = draw.strip().split(" ")
            if color not in map:
                map[color] = int(count)
            else:
                map[color] = max(map[color], int(count))
    return (game_id, map)


with open('day02-input.txt', 'r') as f:
    game_bag_state = {
        'red': 12,
        'blue': 14,
        'green': 13,
    }

    answer = 0
    for line in f:
        line = line.strip()
        (game_id, max_draws_by_color) = parse_input_line(line)
        count = True
        for color in max_draws_by_color.keys():
            if max_draws_by_color[color] > game_bag_state[color]:
                count = False
                break
        if count:
            answer += game_id
    print(answer)
