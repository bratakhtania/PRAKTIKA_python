from sqlite3 import *

conct = connect('mydb.db')
cursor = conct.cursor()


class HomeLib:
    def __init__(self,numb,slov):
        self.numb = numb
        self.slov = slov

    def __str__(self):
        return f'ID: {self.numb}\n' \
               f'Author: {self.slov["author"]}\n' \
               f'Name: {self.slov["name"]}\n' \
               f'Vudav: {self.slov["vudav"]}\n' \
               f'Genre: {self.slov["genre"]}\n' \
               f'Year of start: {self.slov["year"]}\n'


def create_db():
    cursor.execute("CREATE TABLE lib (id text, author text, name text, vudav text, genre text, year text)")


def search(numb, key):
    book = get_book(numb)
    try:
        return book.slov[key]
    except KeyError:
        return 'Wrong key'


def add_book(numb, slov):
    book = HomeLib(numb, slov)
    cursor.execute(f"""INSERT INTO lib VALUES (
                    '{book.numb}',
                    '{book.slov["author"]}',
                    '{book.slov["name"]}',
                    '{book.slov["vudav"]}',
                    '{book.slov["genre"]}',
                    '{book.slov["year"]}')""")
    conct.commit()


def delete_book(numb):
    cursor.execute(f"DELETE FROM lib WHERE id={numb}")
    conct.commit()


def get_book(numb):
    cursor.execute(f"SELECT * FROM lib WHERE id={numb}")
    rows = cursor.fetchall()
    data = rows[0]
    book = HomeLib(data[0], {'author': data[1],
                                    'name': data[2],
                                    'vudav': data[3],
                                    'genre': data[4],
                                    'year': data[5]})
    return book


def main():
    choice = ['1. Add book into libriary: ',
            '2. Delete some book: ',
            '3. Get info about book by id:',
            '4. Search in libriary',
            '5. Exit']
    for comand in choice:
        print(comand)
    comand = input("Select command: ")
    if comand == '1':
        numb = input('Enter id(number of book): ')
        slov = {'author': input('Enter Author of book: '),
                      'name': input('Enter name of book: '),
                      'vudav': input('Enter vudavnutstvo: '),
                      'genre': input('Enter genre of book: '),
                      'year': input('Enter year of start: ')}
        add_book(numb, slov)
        print('Book was added')
    elif comand == '2':
        delete_book(int(input('Enter book id(number): ')))
        print('Book was deleted')
    elif comand == '3':
        print(get_book(int(input('Enter book id(number): '))))
    elif comand == '4':
        print(search(int(input('Enter book id(number): ')), input('Enter key: ')))
    elif comand == '5':
        exit()
    else:
        print("Not exist command")


try:
    create_db()
except OperationalError:
    pass
while True:
    main()
