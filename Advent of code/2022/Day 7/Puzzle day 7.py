D = str(7)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   lis = file.read().split('\n')

infolder = 0
folders = []
folderhistory = []
g = 0
folderdirs = {}
candidate = ('folderx', 1000000000)
sum = 0
true = True

while true:
   sum_main_dir = 0
   currentfolder = '/'
   for i in range(len(lis)):
      if lis[i][0] == '$':
         if lis[i][2:4] == 'cd':
            cfolder = lis[i].split(' ', 2)[2]
            folder = currentfolder + '/' + lis[i].split(' ', 2)[2]
            if cfolder == '/':
               infolder = 0
            elif cfolder == '..' and infolder!= 0:
               infolder -= 1
            else:
               if not any(present == cfolder for present, x in folders) and infolder == g:
                  folders.append((folder, 0))
               if infolder == g:
                  currentfolder = folder
               infolder += 1

      elif lis[i][0].isdigit() and infolder > g:
         folderindex = next(n for n, (folder_name, x) in enumerate(folders) if folder_name == currentfolder)
         digit = int(lis[i].split(' ')[0])
         folders[folderindex] = (folders[folderindex][0], int(folders[folderindex][1])+digit)
      if lis[i][0].isdigit():  
         sum_main_dir += int(lis[i].split(' ')[0])
   g += 1
   if folders == []:
      true = False
   else:
      folderdirs['folders level ' + str(g)] = folders
      folders = []

space_required = 30000000 - (70000000 - sum_main_dir)

for i in range(len(folderdirs)):
   dir = 'folders level ' + str(i+1)
   for x in range(len(folderdirs[dir])):
      if folderdirs[dir][x][1] <= 100000:
         sum += folderdirs[dir][x][1]
      if (folderdirs[dir][x][1] >= space_required) and (folderdirs[dir][x][1] < candidate[1]):
         candidate = folderdirs[dir][x]


print('The total sum of folders with a size of at most 100000 is ' + str(sum) + '.')
print('The best folder to delete would be ' + str(candidate[0].split('/')[-1]) + ' with a total size of ' + str(candidate[1]) + '.')