from typing import Match


tg=[1,2,3,12,2,33,7]

m = tg[6]

for i in tg:
    if m>i:
        m=i
    else:
        m=m

print(m)