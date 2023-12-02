D = str(1)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   lis = file.read().split('\n')

numbers, it, numbers2, cal_values2, cal_values, numbers_written = [], [], [], [], [], ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Part 1 in one line
print(sum([int(str([character for character in line if character.isnumeric()][0])+str([character for character in line if character.isnumeric()][-1])) for line in open('Day '+D+'/Input day '+D+'.txt', 'r').read().splitlines()]))

for i in range(len(lis)):
   numbers.append([character for character in lis[i] if character.isnumeric()])
   cal_values.append(int(str(numbers[i][0])+str(numbers[i][-1])))

   for x in range(len(numbers_written)):
      if numbers_written[x] in lis[i]:
         lis[i] = lis[i].replace(numbers_written[x], numbers_written[x][0] + str(x+1) + numbers_written[x][-1])
         
   numbers2.append([character for character in lis[i] if character.isnumeric()])
   cal_values2.append(int(str(numbers2[i][0])+str(numbers2[i][-1])))

print('Part 1: ' + str(sum(cal_values)) + '\nPart 2: ' + str(sum(cal_values2)))
