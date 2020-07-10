import os.path

with open(os.path.join('file9.txt'), 'r') as in_file, open(os.path.join('file99.txt'), 'w') as out_file:
    for line in in_file:
        out_file.write(line)
    print('Відкрийте файл. Посортовано!\n')
    
with open(os.path.join('file9.txt'), 'r') as in_file, open(os.path.join('file99.txt'), 'w') as out_file:
 inp=in_file.readlines()
 inp.reverse()
 in_file.seek(0)
 out_file.write(''.join(inp))
 print('Відкрийте файл.Посортовано в зворотньому порядку\n')

