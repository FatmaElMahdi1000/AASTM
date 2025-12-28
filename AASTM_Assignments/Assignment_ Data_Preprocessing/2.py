import matplotlib.pyplot as plt
import numpy as np

x =[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
Business = [1780, 1800, 1700, 1865, 1950, 2000, 2000, 2130, 2180, 2200]
Engineering = [1605, 1750, 1770, 1500, 1850, 2000, 2050, 2050, 2100, 2120]
x_arr = np.array(x)
Business_arr = np.array(Business)
Engineering_arr = np.array(Engineering)
Logistics = [1400, 1420, 1350, 1400, 1450, 1560, 1630, 1785, 1820, 1850]
Logistics_arr = np.array(Logistics)
plt.plot(x_arr, Business_arr, label="Business",marker="o", color="r")
plt.plot(x_arr,Engineering_arr, label="Engineering", marker="s", color="blue")
plt.plot(x_arr, Logistics_arr, label="Logistics", marker="d", color="green")
plt.legend()
plt.xlabel("Duration")
plt.ylabel("Number of students")
plt.show()