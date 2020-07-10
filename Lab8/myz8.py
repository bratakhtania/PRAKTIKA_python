class Transport:
    def __init__(self, price, speed, year):#конструктор з параметрами транспортів
        self.price = price
        self.speed = speed
        self.year = year
    def print(self):
        print(self.__class__.__name__)
        print('Ціна поїздки на транспорті: ', self.price)
        print('Швидкість транспорту: ', self.speed)
        print('Рік випуску транспорту:', self.year)
    def Search_for_key(mas, key): #функція пошуку інформації про транспорт за конкретною ознакою
        trig=True
        for i in range(len(mas)):
            for j in range(len(mas[i])):
                if mas[i][j] == key:
                    m=i
                    print('Шуканий параметр має\nТранспорт №',i+1,'з такими параметри:')
                    trig = False
                    for l in range(len(mas[i])):
                        print(mas[m][l],end=' ')
                    print()
        if trig==True:
            print('Транспорту з таким значенням немає!')
        print()
        print()        
    def AddPlan():
       price = input('Введіть ціну поїздки:')
       speed = input('Введіть швидкість:')
       year = input('Введіть рік випуску:')
       high = input('Введіть висоту польоту:')
       passengers = input('Введіть к-сть пасажирів:')
       pl4=(price, speed, year, high, passengers)
       masPlan.append(pl4)
       print('Успішно додано!')
    def AddAuto():
       price = input('Введіть цінупохздки:')
       speed = input('Введіть швидкість:')
       year = input('Введіть рік випуску:')
       motor = input('Введіть назву мотору:')
       aut4=(price, speed, year, motor)
       masAuto.append(aut4)
       print('Успішно додано!')
    def AddShip():
       price = input('Введіть цінупохздки:')
       speed = input('Введіть швидкість:')
       year = input('Введіть рік випуску:')
       port = input('Введіть потр призначення:')
       passengers = ('Введіть к-сть пасажирів:')
       shp4=(price, speed, year, port, passengers)
       masShip.append(shp4)
       print('Успішно додано!')
    
class Plan(Transport):
    def __init__(self, price, speed, year, high, passengers):
        Transport.__init__(self, price, speed, year)#запозичення загальних змінних з батьківського класу
        #змінні цього класу
        self.high = high
        self.passengers = passengers
    def print(self):
        print("Модель    Швидкість     Рік     Висота     Пасажири    ")
        super().print()#ВИКЛИК ФУНКЦІЇ БАТЬКІВСЬКОГО КЛАСУ
        #виклик функції субкласу
        print('Висота підйому літака: ',self.high)
        print('К-сть пасажирів літака: ',self.passengers)
        print()
 
class Auto(Transport):
     def __init__(self, price, speed, year, motor):
        Transport.__init__(self, price, speed, year)
        self.motor = motor
     def print(self):
        print("Модель    Швидкість     Рік     Мотор    ")
        super().print()
        print('Мотор автомобіля: ',self.motor)
        print()
    
class Ship(Transport):
     def __init__(self, price, speed, year, port, passengers):
         Transport.__init__(self, price, speed, year)
         self.port = port
         self.passengers = passengers
     def print(self):
        print("Модель   Швидкість    Рік    Порт    Пасажири   ")
        super().print()
        print('Порт призначення корабля: ',self.port)
        print('К-сть пасажирів корабля: ',self.passengers)
        print()

pl1=Plan(120,'2000km/h',2015,7000,250)
pl2=Plan(500,'5000km/h',2019,3000,100)
pl3=Plan(200,'4000km/h',2017,5000,300)
masPlan=[[pl1.price,pl1.speed,pl1.year,pl1.high,pl1.passengers],
       [pl2.price,pl2.speed,pl2.year,pl2.high,pl2.passengers],
       [pl3.price,pl3.speed,pl3.year,pl3.high,pl3.passengers]]

aut1=Auto(100,'200km/h',2016,111)
aut2=Auto(300,'250km/h',2020,222)
aut3=Auto(450,'300km/h',2011,333)
masAuto=[[aut1.price,aut1.speed,aut1.year,aut1.motor],
       [aut2.price,aut2.speed,aut2.year,aut2.motor],
       [aut3.price,aut3.speed,aut3.year,aut3.motor]]

shp1=Ship(600,'100km/h',2000,'AmericaPort',250)
shp2=Ship(700,'600km/h',1998,'Legas',100)
shp3=Ship(1000,'500km/h',2008,'St.Marino',300)
masShip=[[shp1.price,shp1.speed,shp1.year,shp1.port,shp1.passengers],
       [shp2.price,shp2.speed,shp2.year,shp2.port,shp2.passengers],
       [shp3.price,shp3.speed,shp3.year,shp3.port,shp3.passengers]]

print('''Вітаємо в транспортній компанії!\nЯк можу Вам допомогти:
1 - Оглянути наявний транспорт
2 - Знайти транспорт за його параметром
3 - Додати транспорт''')
while True:
    print("Введіть номер команди:")
    command = input()
    if command == '1':
        print('''Який вид транспорту ви хочете оглянути:
              p - Літаки
              a - Автомобілі
              s - Кораблі''')
        print('Введіть знак транспорту: ')
        z=input()
        if z=='p':
         pl1.print()
         pl2.print()
         pl3.print()
        elif z=='a':
         aut1.print()
         aut2.print()
         aut3.print()
        elif z=='s':
         shp1.print()
         shp2.print()
         shp3.print()
        
    elif command == '2':
        print('''Який вид транспорту ви хочете перевірити за параметром:
              p_k - Літаки
              a_k - Автомобілі
              s_k - Кораблі''')
        print('Введіть знак транспорту: ')
        z_k=input()
        if z_k=='p_k':
         Transport.Search_for_key(masPlan,'2000km/h')
        elif z_k=='a_k':
         Transport.Search_for_key(masAuto,111)
        elif z_k=='s_k':
         Transport.Search_for_key(masShip,'St.Marino')
       
    elif command == '3':
        print('''Який вид транспорту ви хочете додати:
              p_d - Літаки
              a_d - Автомобілі
              s_d - Кораблі''')
        print('Введіть знак транспорту: ')
        z_d=input()
        if z_d=='p_d':
         Transport.AddPlan()
        elif z_d=='a_d':
         Transpport.AddAuto()
        elif z_d=='s_d':
         Transport.AddShip()
        
    else:
        print('Невідома команда')



