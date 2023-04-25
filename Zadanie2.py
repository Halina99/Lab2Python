import random

lotto = []
i = 0

while i < 7:
    r = random.randint(1, 49)
    if lotto.count(r) == 0:
        lotto.append(r)
        i+=1
print(lotto)