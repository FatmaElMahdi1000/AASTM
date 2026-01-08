import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns #for adjusting plot style
sns.set_style('darkgrid') #must be called before start plotting
np.random.seed(0)
a = np.random.randint(10, size=5)
b = np.random.randint(10, size=5)
c = np.random.randint(12, size=5)
data = {'a': a, 'b': b, 'c': c}
df = pd.DataFrame(data)
# fig = plt.figure(figsize=(10,5)) #returning and empty figure
# ax1 = plt.subplot(2,1,1)
# ax2 = plt.subplot(2,1,2)
fig, ax = plt.subplots(3, 1, figsize=(15,8)) #crearting 2 X 2 grid.

ax[0].plot(df.index.values, df['a'], marker="d", color="b",ls="-.",label="A") #ls stands for line style
ax[1].plot(df.index.values, df['b'], marker="*", color="r",label="B")
ax[2].plot(df.index.values, df['c'],marker="o", color="orange", lw=3,label="C") #lw stands for line width
# ax[3].plot(df.index.values, np.arange(len(df)), marker="D", color="green", lw=1 ,label="D") #creates an array that acts as the y-axis, with a length that's equal to df length (5 rows)
ax[0].legend()
ax[1].legend()
ax[2].legend()
# ax[3].legend()
plt.show()
