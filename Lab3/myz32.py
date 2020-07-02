import random
n = int(input('Введіть кількість елементів n: \n'))
m = int(input('Введіть кількість елементів m:\n'))

from random import randint
arr = [[randint(-10, 10) for j in range(n)] for i in range(m)]  
print('Our matrix:',arr)

posi=0
posj=0
max_elem = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i] )):
         if (arr[i][j] < max_elem)and(arr[i][j] < 0):
               max_elem =  arr[i][j]
               posj=j
               posi=i
print('Max elem:',max_elem,', posi=',posi,',posj=',posj)

posii=0
posjj=0
min_elem = arr[0][0]               
for i in range(len(arr)):
    for j in range(len(arr[i] )):
         if (arr[i][j] < min_elem)and(arr[i][j] > 0):
               min_elem =  arr[i][j]
               posjj=j
               posii=i
print('Min elem:',min_elem,', posii=',posii,',posjj=',posjj)

cols = (posj,posjj)
for row in arr: print(row);print('\n')
swap = [ row[cols[posjj]] for row in arr ]
for row in arr: row[cols[posjj]] = row[cols[posj]]
for i, row in enumerate(arr): row[cols[posj]] = swap[i]
for row in arr: print(row)

