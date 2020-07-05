from myz62 import *
l=[1,1,4,8,2,4]
sort(l)
print('\n')
znachElem(l,4)
print('\n')
print('Введіть список у якому шукатимете послідовності:')
listnew=input().split()
print('Введіть послідовність, яку ви шукаєте:')
trig=input().split()
if(poslidElem
   (listnew,trig)==True):
    print('Така послідовність існує!')
else:
    print('Немає такої послідовності')
print('\n')
Minfive(l)
print('\n')
Maxfive(l)
print('\n')
Suma(l)
print('\n')
noident(l)
