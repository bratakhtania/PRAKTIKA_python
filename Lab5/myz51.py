d={'ab':'apple', 3:'pen'}
for key in d:
    print('Доступні ключі',key)
    
def my_dict(key1,dictionary):
    
    for key in dictionary:
        if key1==key:
            print(key1, '->',dictionary[key1])
            break
        elif key1!=key:
         continue
k=input('Оберіть ключ:')
print('Ключ:',k)         
my_dict(k,d)
  
