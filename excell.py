
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel (r'C:\Users\wn49s\AppData\Local\Programs\Python\Python38-32\ages.xlsx', header=None)

a =df.loc[1].values.tolist()
b=df.loc[2].values.tolist()
c=df.loc[3].values.tolist()
d =df.loc[4].values.tolist()
e=df.loc[5].values.tolist()
f=df.loc[6].values.tolist()

fig, ax = plt.subplots()

ax.set(xlabel='Date in May', ylabel='Deaths',
       title='Deaths by age group')
ax.plot(f, a,label='0 – 19')

ax.plot(f, b,label='20 – 39')


ax.plot(f, c,label='40 – 59')
ax.plot(f, d,label='60 – 79')
ax.plot(f, e,label='80+')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)


plt.legend()

plt.show()








