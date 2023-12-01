with open('Day 1/Input day 1.txt', 'r') as file:
   list = file.read().split('\n')
elves = []

for i in range(list.count('')-1):
    start = [i for i, n in enumerate(list) if n == ''][i] +1
    end = [i for i, n in enumerate(list) if n == ''][i+1]
    append = sum([eval(i) for i in list[start:end]])
    if append > 0:
        elves.append(append)
elf1 = elves.index(max(elves)) +1
cal_elf1 = elves[elf1-1]
del elves[elf1-1]
elf2 = elves.index((max(elves))) +1
cal_elf2 = elves[elf2-1]
del elves[elf2-1]
elf3 = elves.index((max(elves))) +1
cal_elf3 = elves[elf3-1]

print('Elf ' + str(elf1) + ' is carrying the most callories with a total of ' + str(cal_elf1) + ' in their bag.')
print('Elf ' + str(elf2) + ' is carrying the second most callories with a total of ' + str(cal_elf2) + ' in their bag.')
print('Elf ' + str(elf3) + ' is carrying the third most callories with a total of ' + str(cal_elf3) + ' in their bag.')
print('Elf ' + str(elf1) + ', ' + str(elf2) + ' and ' + str(elf3) + ' are carrying a total of ' + str(cal_elf1+cal_elf2+cal_elf3) + ' callories.')
