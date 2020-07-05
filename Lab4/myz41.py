groups = []
for i, val in enumerate('   c b     ddd '):
    if i == 0:
         cnt = 1
         loc = i
         last_val = val
    elif val == last_val:
         cnt += 1
    else:
         groups.append((cnt, last_val, loc))
         cnt = 1
         loc = i
         last_val = val

for group in groups:
    for last_val in group:
        if last_val == ' ':
         print("group of {0} {1}'s found at index {2}".format(*group))
max_zn = max(groups)
print("Група з максимальним числом пробілів: ",max_zn)
