import math
import itertools

def f(x,k):
    return pow(-1,k-1)*((2*pow(x,k))/math.factorial(k)) 
e=0.001
a=-3
b=2
k=0
i=0
for x in itertools.count(start=a,step=0.5):
    if x>b:
        break
    tmp=f(x,k)
    resault=tmp
    ex = pow(math.e,2*x)
    while(abs(tmp)>=e):
            k+=1
            i+=1
            tmp=f(x,k)
            resault+=x
            
    print('x=',x)
    print('Результат точно обчисленої функції з модуля math:',ex)
    print("Результат: ", resault)
    print('Точність:',e)
    print('К-сть ітерацій:', k)
    print('-----------------------------------------------')
print('Загальна к-сть ітерацій:',k)
            
