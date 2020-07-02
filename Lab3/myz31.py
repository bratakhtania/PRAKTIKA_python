import random
n = int(input('Введіть кількість елементів n: \n'))
my_list=random.sample(range(-10,10),n)
print('Our list:',my_list)

max = my_list[0]
pos = 0
for i in range(len(my_list)):
    if my_list[i]>max: max=my_list[i];pos=i
print ("Max el=",max,", pos=",pos)
myl=[]                  
for i in range(len(my_list)):
    if my_list[i]!=my_list[pos]:
     my_list[i]=my_list[i]**2
     myl.append(my_list[i])
    else:
     break
print(myl)
