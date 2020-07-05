text = set("BratakhTanniaEunaitivnaObydri")
vowl = 0
const = 0
new = set()
for i in text:
    bukva = i.lower()
    if bukva == "a" or bukva == "e" or\
       bukva == "i" or bukva == "o" or\
       bukva == "u" or bukva == "y":
        vowl += 1
        new.add(bukva)
    else:
        const += 1
new1=list(new)
new1.sort()

print("Голосні: %s\n Приголосні: %s" % (vowl, const))
print(new1)
