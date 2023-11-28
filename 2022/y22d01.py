from aocd import get_data, submit
from dotenv import load_dotenv

import heapq

load_dotenv()

DAY = 1
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
data_list: list[str] = data.split('\n')

total_list = []
while data_list:
    cur_total = 0
    while data_list and data_list[0] != '':
        cur_total += int(data_list.pop(0))
    heapq.heappush(total_list, -cur_total)
    if data_list:
        data_list.pop(0)
    else:
        break

part1 = -heapq.heappop(total_list)
part2 = part1 + -heapq.heappop(total_list) + -heapq.heappop(total_list)

submit(part1, part="a", day=DAY, year=YEAR)
submit(part2, part="b", day=DAY, year=YEAR)
