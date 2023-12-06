with open('Input/Day 6.txt', 'r') as file:
   lis = file.read().split('\n')

rtimes = [int(time) for time in lis[0].split(' ') if time != '' and ':' not in time]
rdistances = [int(distance) for distance in lis[1].split(' ') if distance != '' and ':' not in distance]
rtime, rdistance = int(''.join([str(x) for x in rtimes])), int(''.join([str(x) for x in rdistances]))
answer1, answer2 = 1, 0

for time in range(len(rtimes)):
    methods = 0
    for milliseconds in range(rtimes[time]):
      if ((rtimes[time]-milliseconds)*milliseconds) > rdistances[time]:
          methods += 1
    answer1 *= methods

for milliseconds in range(rtime):
      if ((rtime-milliseconds)*milliseconds) > rdistance:
          answer2 += 1

print(f'Answer for part 1: {answer1}\nAnswer for part 2: {answer2}')