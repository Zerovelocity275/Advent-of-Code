import copy

D = str(6)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   datastream = file.read()

marker_length = 14

for i in range(len(datastream)):
   marker, unique = datastream[i:i+marker_length], True
   for x in marker:
        if marker.count(x) > 1:
            unique = False
   if unique:
      firstmarkerat = i+marker_length
      break

print('First marker is ' + marker + ' after ' + str(firstmarkerat) + ' characters.')