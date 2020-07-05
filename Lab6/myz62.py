def sort(mas): #1 
    mas.sort() #впорядковую(сортує)
    for i in range(len(mas)): #для всієї довжини 
        print(mas[i],' ')

def znachElem(mas, key): #2
    for i in range(len(mas)):
        if mas[i] == key: # якщо значення введене дорівнює значенню в списку
            print('Таке значення Є:',mas[i])
            break
def poslidElem(mas,key):              #3
    check = False
  #цикл по 1-му списку
    for m in mas: 
        #цикл по 2-му списку(слові) 
        for n in key: 
            #якщо знаходить якесь спільне
            if m == n: 
                trig = True #змінюємо тригер
                return trig             
    return check

def Minfive(mas): #4
    mas.sort() #сортуємо
    for i in range(0,5): # виводимо тільки 5 перших 
        print(mas[i],' ')

def Maxfive(mas): #5
    mas.sort(reverse=True) # обертаємо в зворотньому порядку
    for i in range(0,5): # виводимо перших 5
        print(mas[i],' ')

def Suma(mas): #6
    s=sum(mas)/len(mas) #формула середнього арифметичного
    print(s)
    
def noident(mas): #7
   nomas = list(set(mas)) #перетворення в множину для забирання ідентичних(повторюваних) елементів
   print(nomas)
   
