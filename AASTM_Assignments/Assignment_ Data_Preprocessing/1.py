import numpy as np
import matplotlib.pyplot as plt

Names = ['Amr', 'Mai', 'Aya', 'Sam', 'Ali', 'Ola', 'Bob', 'Lee']
Marks =  [56, 78, 93, 42, 97, 85, 34, 86]
Names_arr = np.array(Names)
Marks_arr = np.array(Marks)

plt.bar(Names_arr, Marks_arr, color="b")
plt.show()
print(f"Average marks:{np.average(Marks)}")
#success %
passed = Marks_arr[Marks_arr >= 50]
success_percentage = (len(passed) / len(Marks_arr)) * 100
print(f"Success percentage: {success_percentage} %")