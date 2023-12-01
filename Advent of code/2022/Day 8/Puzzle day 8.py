D = str(8)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   lis = file.read().split('\n')

top, side = {}, {}

for i in range(len(lis)):
   side[i+1] = list(lis[i])

for i in range(len(side[1])):
   for x in range(len(side)):
      top[i] = side[x][i]



