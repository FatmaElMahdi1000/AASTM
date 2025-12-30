import matplotlib.pyplot as plt
import numpy as np
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
y_values = np.array(doubling_array)
x_values = np.arange(1,len(doubling_array)+1)

plt.scatter(x_values, y_values, marker="D") #for label here we need, plt.legend() to show the label
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Data Camp Exercise")
# plt.legend()
plt.show()