class HomeLib:
    def __init__(self, numb, slov): #конструктор який приймає ціле число та словник
        self.numb = numb
        self.slov = slov
        
    def SearchBook(self,key1,key2,slov):#пошук книги за декількома параметрами
        trig=True
        for i in slov:
            if slov['Author'] == key1:
                for j in slov:
                    if slov['Year']==key2:
                        trig = False
        if trig==True:
            print('Такої книги немає в наявності!')
        else:
            print("Книга: ",slov['Numb'],slov['Author'],slov['Name'],slov['Vudav'],slov['Genre'],slov['Year'])

    def SearchNumBook(key,slov): #пошук будь-якої книги за номером
        trig=True
        for i in slov:
            if slov['Numb']== key:
                trig = False
        if trig==True:
            print('Книги з таким номером немає!')
        else:
            print("Книга з номером: ",slov['Numb'],slov['Author'],slov['Name'],slov['Vudav'],slov['Genre'],slov['Year'])

    def AddBook(): #додавання нової книги
        numb = input("Номер книги:")
        author = input("Автор: ")
        name = input("Ім'я: ")
        vudav = input("Видавництво: ")
        genre = input("Жанр: ")
        year = input("Рік видання: ")
        slov = {'Numb':numb,'Author':author,'Name':name,'Vudav':vudav,'Genre':genre,'Year':year}
        return slov
    
    def DelBook(name,slov,slovn,slovn1):#видалення будь-якої книги за номером
        if name in slov['Name']:
            del slov
            return print("Книга з ім'ям ",name, "видалена")
        if name in slovn['Name']:
            del slovn
            return print("Книга  ",name,"була видалена")
        if name in slovn1['Name']:
            del slovn1
            return print("Книга під ім'ям ",name,"була видалена")
        return print('Книга відсутня!')
    
#головна програма
    
slovnuk = {'Numb':1,'Author':'Skrupka','Name':'Kolobok','Vudav':'IFbook','Genre':'lyric','Year':2000}
slovnuk1 = {'Numb':2,'Author':'Shevchenko','Name':'100 YEARS','Vudav':'Ababagalamaga','Genre':'poem','Year':1992}
obj = HomeLib(1, slovnuk)
print('Знайдемо книгу за автором Skrupka та 2000 роком: ')
obj.SearchBook('Skrupka',2000,slovnuk)
print('Додамо нову книгу. Введіть інформацію про неї:')
slovnuk2=HomeLib.AddBook()
print('Видалимо книгу з імям Kolobok:')
HomeLib.DelBook('Kolobok',slovnuk, slovnuk1,slovnuk2)
print('Знайдемо книгу з номером 2:')
HomeLib.SearchNumBook(2,slovnuk1)
print('----------------------------------------------')
