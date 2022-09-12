import kDict
import logging


# falla con mechant

# logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

#w = input("Introduce un termino: ")
w = "méchant"

'''
print(w + " según LeRobert....")
d = kDict.kDict(w)
ms = d.lerobert()
n = 1
for m in ms:
    print(str(n) + ".- " +m)
    n+=1
    '''

print(w + " según Wiktionary....")
d = kDict.kDict(w)
ms = d.wiktionary()
n = 1
for m in ms:
    print(str(n) + ".- " +m)
    n+=1    