import matplotlib.pyplot as plt
import numpy as np

print("Enter your GPA along the 8 semesters... ")
GPAs = []
semesters = []
for i in range(1, 9):
    GPA = float(input(f"Semester ({i}): "))
    GPAs.append(GPA)
    semesters.append(i)

GPAs_arr = np.array(GPAs)
print(f"Mean = {np.mean(GPAs_arr)}")
print(f"Median = {np.median(GPAs_arr)}")
print(f"standard deviation = {np.std(GPAs_arr)}")
print(f"Highest Achievement: {np.max(GPAs_arr)}")
print(f"Lowest Achievement: {np.min(GPAs_arr)}")
#Plotting
semesters_arr = np.array(semesters)
plt.plot(semesters_arr, GPAs_arr, ls=" ", marker="d", color="r")
plt.show()