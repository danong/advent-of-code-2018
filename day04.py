import datetime
from collections import defaultdict

with open('input/day04.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]
inp = sorted(inp)
day = [False] * 60

cur_guard = None
cur_date = None
sleep_start = None
cur_day = None
sleep_schedule = defaultdict(list)
for entry in inp:
    date = entry.split(' ')[0][1:]
    date = datetime.date(*(int(x) for x in date.split('-')))
    time = entry.split(' ')[1][:-1]
    message = entry.split(' ')[2:]

    if message[0] == 'Guard':
        if cur_day:
            sleep_schedule[cur_guard].append(cur_day)
        cur_guard = message[1]
        cur_day = [False] * 60
        if time[0] == '0':
            cur_date = date
        else:
            cur_date = date + datetime.timedelta(days=1)
    elif message[0] == 'falls':
        sleep_start = int(time[3:])
    else:
        sleep_end = int(time[3:])
        for i in range(sleep_start, sleep_end):
            cur_day[i] = True
        sleep_start = None

# part 1
max_sleep = (0, None)
for guard in sleep_schedule:
    sleep = sum(sum(x) for x in sleep_schedule[guard])
    if sleep > max_sleep[0]:
        max_sleep = (sleep, guard)
print(max_sleep)
print(int(max_sleep[1][1:]) * max_sleep[0])
# part 2
max_sleep = (0, None, None)  # sleep count, guard id, sleep id
for guard in sleep_schedule:
    night = [sum(i) for i in zip(*sleep_schedule[guard])]
    if max(night) > max_sleep[0]:
        max_sleep = (max(night), guard, night.index(max(night)))
print(max_sleep)
print()
