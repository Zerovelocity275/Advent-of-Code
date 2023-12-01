D = str(4)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   lis = file.read().split('\n')

elffullycontains = 0
elfoverlap = 0

for i in range(len(lis)):
   elf1 = [int(x) for x in lis[i].split(',')[0].split('-')]
   elf2 = [int(x) for x in lis[i].split(',')[1].split('-')]
   if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
      elffullycontains += 1
   if elf1[0] <= elf2[1] and elf1[1] >= elf2[0]:
      elfoverlap += 1

print('There are ' + str(elffullycontains) + ' elf pairs where one assignments fully encompasses the other and ' + str(elfoverlap) + ' elf pairs where they overlap at all.')