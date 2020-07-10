import os.path 
import datetime 
import io

def read_file(reytung):
    """Функція для зчитування файла fname
та виведення його вмісту на екран"""
    file = open(reytung, 'r')  # відкриття файлу для зчитування
    print('\nФайл ' + reytung + ' відкрито :')  # виведення назви файлу
    # зчитування вмісту файла по рядках
    for line in file:
        print(line, end='')  # виведення рядка s 
 
    file.close()  # закриття файлу 

def write_text_to_file(filename, text):
    """Функція для запису у файл filename рядка text"""
    f = open(filename, "w")  # відкриття файла для запису
    f.write(text)  # Запис рядка text у файл
    f.close()  # Закриття файлу
 
def search_papka(fname):
    print('Знайдемо папку з назвою ',fname,'\n')
    for filename in os.listdir("..\\Lab9"):
        print(filename)
        if filename==fname:
          print('!!!!!Done!!!!!: ',filename)
    print('\n')
def search_file(word,fname):
    for line in open(fname):
        if word in line:
            print('Знайдено в рядку: ',line,end='')
            
def sort_file(fname):
        file = open(fname,'r+')
        list1=file.readlines()
        list1.sort(key=lambda l: float(l.split(" - ")[1]))
        file.seek(0)
        file.write("".join(list1))
        print("Рядки успішно посортовані в файлі",fname,"! Відкрийте файл щоб переглянут: ")
        file.close()


text = '''Паш - 4
Черней - 0''' 
 
text1 = '''Гурей - 4'''
text2 = '''Гриш - 5
Гончар - 3
Сакадел - 4
Братах - 5'''
text3 = '''Пиріг - 5
Кирилюк - 5
Фесняк - 3
Лашків - 3
Семеряк - 5'''
print('''Оберіть, що хочете зробити:
1 - записати в файл
2 - зчитати  з файлу
3 - дописатии в файл
4 - знайти в каталозі файл
5 - знайти дані в папці
6 - посортувати по середньому балу рядки з студентами
7 - вийти''')

while True:
 print('Введіть команду: ')
 k=input()
 if k=='1':      
  read_file(os.path.join('reytung1.txt'))
  read_file(os.path.join('reytung2.txt'))
  continue
 elif k=='2':
  write_text_to_file(os.path.join('reytung1.txt'), text)
  write_text_to_file(os.path.join('reytung2.txt'), text1)

  read_file(os.path.join('reytung1.txt'))
  read_file(os.path.join('reytung2.txt'))
  print('\n')
 elif k=='3':
  log_file = os.path.join('reytung1.txt')
  with open(log_file, 'a') as log:
   print('\n',text2,file=log)
  log_file = os.path.join('reytung2.txt')
  with open(log_file, 'a') as log:
   print('\n',text3,file=log)
   
  read_file(os.path.join('reytung1.txt'))
  read_file(os.path.join('reytung2.txt'))
 elif k=='4':
  search_papka(os.path.join('reytung1.txt'))
  search_papka(os.path.join('reytung2.txt'))
 elif k=='5':
    search_file('Паш',os.path.join('reytung1.txt'))
    search_file('Гурей',os.path.join('reytung2.txt'))
 elif k=='6':
  sort_file(os.path.join('reytung1.txt'))
  sort_file(os.path.join('reytung2.txt'))
 elif k=='7':
    break
 else:
     print('Невідома команда')
     continue

