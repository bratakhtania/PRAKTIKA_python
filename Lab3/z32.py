# Створення списку чисел
my_list  =  [5, 7, 9, 1, 1, 2]
# Отримання передостаннього значення
pre_last  =  my_list  [-2] #  pre_last  ==  «1»
print(pre_last)
# Обчислення суми першого і останнього значень
result  =  my_list[0]  +  my_list[-1];print(result) 
  
my_list  =  [5, 7, 9, 1, 1, 2] #  Створення  списку  чисел
# Отримання зрізу списка від нульового (першого) елемента
# (включаючи його) до третього (четвертого) (не включаючи)
sub_list  =  my_list[0:3]
print(sub_list) #  Виведення  отриманого  списку
# Виведення елементів списка від другого до передостаннього
print(my_list[2:-2])
#  Виведення  ел-тів  списка  від  4-ого  (5-ого)  до  5-ого  (6-ого)
print(my_list[4:5]) 
 
my_list  =  [5, 7, 9, 1, 1, 2]
#  Вибір  кожного  другого  ел-та  списку  (починаючи  з  першого), # не включаючи останній елемент
sub_list  =  my_list[0:-1:2]
print(sub_list) #  виведення  отриманого  списку
# Виведення елементів від 2-ого (3-ього) до передостаннього   # з кроком 2
print(my_list[2:-2:2])
#  Виведення  ел-тів  списка,  крім  першого,  в  зворотному порядку
print(my_list[-1:0:-1]) 
 
 
my_list=[5, 7, 9, 1, 1, 2]
# Виведення елементів списка від 2-ого (3-ього) значення до кінця
print(my_list[2:])
#  Виведення  всіх  ел-тів  списка  від  початку  до передостаннього ел-та
print(my_list[:-2])
# Виведення всіх елементів списку в зворотному порядку
print(my_list[::-1]) 
 
