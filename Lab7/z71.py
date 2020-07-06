class Student: 
 
    def set_marks(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3  
 
    def __init__(self, name=""):
        self.name = name 
 
    
    def get_average_mark(self):
        print(self.name, ' - ', ((self.e1 + self.e2 + self.e3) / 3)) 
 
k=int(input('Введіть кількість студентів:'))
i=0
for i in range(k):
    print('Введіть імя студента:')
    s=Student()
    s.name=input()
    m1=int(input('Введіть 1 оцінку студента:'))
    m2=int(input('Введіть 2 оцінку студента:'))
    m3=int(input('Введіть 3 оцінку студента:'))
    s.set_marks(m1,m2,m3)
    s.get_average_mark()
    print('\n')
       
 

