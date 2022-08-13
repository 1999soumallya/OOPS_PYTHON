x=3
y=1
while (y!=x):
    print(y)
    y=y+1

class car(object):
    make="Honda"
    model="Accord"
    color="Blue"
    def display(cls):
        print(cls.make,cls.model,cls.color)

c=car()
c.display()

A=['1','2','3']
for a in A:
    print(2*a)

'''import pandas as bananna
df=bananna.DataFrame({'a':[11,21,31],'b':[21,22,33]})
df.head()'''

import pandas as pd
df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
df['a']==1