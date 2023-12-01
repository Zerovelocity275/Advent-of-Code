import string

Day = str(3)
with open('Day ' + Day + '/Input day ' + Day + '.txt', 'r') as file:
   lis = file.read().split('\n')

Priority = list(string.ascii_letters)
RugsackC1 = []
RugsackC2 = []
Matching = []
Badges = []
Tot_priority1 = 0
Tot_priority2 = 0

for i in range(len(lis)):
    RugsackC1.append(str(lis[i])[0:int(len(lis[i])/2)])
    RugsackC2.append(str(lis[i])[int(len(lis[i])/2):int(len(lis[i]))])
    Matching.append(set(RugsackC1[i]).intersection(RugsackC2[i]))

for n in range(int(len(lis)/3)):
    Group = []
    i = n*3
    for x in range(2):
        Group.append(set(lis[i]).intersection(lis[i+x+1]))
    Badges.append(set(Group[0]).intersection(Group[1]))

for i in range(len(Matching)):
    Tot_priority1 += int(Priority.index(list(Matching[i])[0]))+1
for i in range(len(Badges)):
    Tot_priority2 += int(Priority.index(list(Badges[i])[0]))+1

print(Tot_priority1)
print(Tot_priority2)