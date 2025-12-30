import numpy as np
arr=[1,2,1,12,34,1]
a = np.array(arr)

for x in a:
    if x == 0:
        print("zero exist!")
        break
else:
    print("No zeros at all!")
#another Method
print(np.any(a == 0)) #
print(np.all(a != 0))