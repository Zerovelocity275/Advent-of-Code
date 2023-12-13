with open('Input/Day 13.txt', 'r') as file:
   patterns = [[list(line) for line in pat.split('\n')] for pat in file.read().split('\n\n')]

def ax_change(pat):
    return [list(row) for row in zip(*pat)]

def notes(rows, smudge):
    total = 0
    for row in range(len(rows)-1):
        for i in range(min(row+1, len(rows)-row-1)):
            if sum(x != y for (x, y) in zip(rows[row-i], rows[row+i+1])) <= smudge:
                mirrored = True
            else:
                mirrored = False
                break
        if mirrored:
            total+=row+1
    return total

answer1 = sum([notes(pat, 0)*100 + notes(ax_change(pat), 0) for pat in patterns])

print(f'Answer for part 1: {answer1}\nAnswer for part 2: {sum([notes(pat, 1)*100 + notes(ax_change(pat), 1) for pat in patterns])-answer1}')
