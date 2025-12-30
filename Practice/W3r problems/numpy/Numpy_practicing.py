# import numpy as np
# sudoku_list =[
#  [0, 0, 4, 3, 0, 0, 2, 0, 9],
#  [0, 0, 5, 0, 0, 9, 0, 0, 1],
#  [0, 7, 0, 0, 6, 0, 0, 4, 3],
#  [0, 0, 6, 0, 0, 2, 0, 8, 7],
#  [1, 9, 0, 0, 0, 7, 4, 0, 0],
#  [0, 5, 0, 0, 8, 3, 0, 0, 0],
#  [6, 0, 0, 0, 0, 0, 1, 0, 5],
#  [0, 0, 3, 5, 0, 8, 6, 9, 0],
# [0, 4, 2, 9, 1, 0, 3, 0, 0]
# ]
# sudoku_array = np.array(sudoku_list)
# print(type(sudoku_array)) #it prints the type of the list.
import numpy as np

# Create an array of zeros which has four columns and two rows
zero_array = np.zeros((2, 4))
print(zero_array)

# Create an array of random floats which has six columns and three rows
random_array = np.random.random((3, 6))
print(random_array)