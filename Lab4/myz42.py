text = set("BratakhTannia20")
vowl = 0
const = 0
zufr = 0
for i in text:
    bukva = i.lower()
    if bukva == "a" or bukva == "e" or\
       bukva == "i" or bukva == "o" or\
       bukva == "u" or bukva == "y":
        vowl += 1
    elif bukva=="0" or  bukva == "1" or\
       bukva == "2" or bukva == "3" or\
       bukva == "4" or bukva == "5" or \
       bukva == "6" or bukva =="7" or \
       bukva == "7" or bukva == "8" or \
       bukva == "9":
        zufr += 1  
    else:
        const += 1
print("Голосні: %s\n Приголосні: %s" % (vowl, const))
