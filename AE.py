
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel (r'C:\Users\wn49s\AppData\Local\Programs\Python\Python38-32\AE.xlsx', header=None)

print (df)


a =df.loc[0].values.tolist()
b=df.loc[1].values.tolist()
c=df.loc[2].values.tolist()

print (a,b,c)



fig, ax = plt.subplots()

ax.set(xlabel='Month', ylabel='A & E Admissions',
       title='A & E Admission Stats')
ax.plot(b, a)





ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)


plt.legend()

plt.show()








