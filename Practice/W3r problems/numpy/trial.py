import numpy as np
np.random.seed(0)
# x1_1D = np.random.randint(10, size=6) #generating random elements from 0 to 10, 1D array
# x2_2D = np.random.randint(10, size=(2,3)) #2 rows_3 elements
#
# x3_3D = np.random.randint(10, size=(3, 4, 5)) #layers,rows, columns
# x5_2D = np.random.randint(10, size=(2,3)) #2 rows_3 elements
# x4_3D_array = np.array([x5_2D, x2_2D]) #2 arrays(layers), with identical rows and colums
# print(np.ndim(x4_3D_array)) #number of dimensional
# print(np.ndim(x2_2D))
# print(np.size(x4_3D_array)) #number of elements in the array/(the total size of the array)
#
#one dimensional subarrays:
# x = np.arange(10)
# print(x)
# print(x[::2])
# print(x[::-1]) #all elments reversed

y_2d = np.random.randint(10, size=(3,3))
print(y_2d)
# print(np.ndim(y_2d)) #type of the dimensional
print(y_2d[:2,:2]) #slicing rows and columns
