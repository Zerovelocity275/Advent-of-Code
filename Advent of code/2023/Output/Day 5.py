with open('Input/Day 5.txt', 'r') as f:
    lis = f.read().split('\n\n')

seedlis = lis[0].split(' ')
seedlis.pop(0)
seed_to_x = {int(x):int(x) for x in seedlis}
seed_to_x2 = [[int(seedlis[2*x]),int(seedlis[2*x])+int(seedlis[2*x+1])-1] for x in range(10)]
convert_dict = {}

for i in range(1, len(lis)):
    convert_dict[lis[i].split(' ')[0]] = {int(line.split(' ')[1]):[int(line.split(' ')[0]), int(line.split(' ')[2])] for line in lis[i].splitlines() if ':' not in line}

for conversion in convert_dict:
    for seed in seed_to_x:
        seed_in = False
        for seed_to in convert_dict[conversion]:
            if seed_to_x[seed] in range(seed_to, seed_to+convert_dict[conversion][seed_to][1]) and not seed_in:
                seed_to_x[seed] = convert_dict[conversion][seed_to][0]+seed_to_x[seed]-seed_to
                seed_in = True
    seed = 0
    while seed < len(seed_to_x2):
        seed_in = False
        for seed_to in convert_dict[conversion]:
            if seed_to_x2[seed][0] in range(seed_to, seed_to+convert_dict[conversion][seed_to][1]) and not seed_in:
                if seed_to_x2[seed][1] < seed_to+convert_dict[conversion][seed_to][1]:
                    seed_to_x2[seed][0] = convert_dict[conversion][seed_to][0]+seed_to_x2[seed][0]-seed_to
                    seed_to_x2[seed][1] = convert_dict[conversion][seed_to][0]+seed_to_x2[seed][1]-seed_to
                else:
                    seed_to_x2[seed][0] = convert_dict[conversion][seed_to][0]+seed_to_x2[seed][0]-seed_to
                    seed_to_x2.append([seed_to+convert_dict[conversion][seed_to][1], seed_to_x2[seed][1]])
                    seed_to_x2[seed][1] = convert_dict[conversion][seed_to][0]+convert_dict[conversion][seed_to][1]-1
                seed_in = True
        seed += 1

print(f"Minimum location 1 is: {min([seed_to_x[location] for location in seed_to_x])}\nMinimum location 2 is: {min([location[0] for location in seed_to_x2])}")