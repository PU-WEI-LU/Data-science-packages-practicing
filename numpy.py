import numpy as np

# 1. Import numpy as np and see the version
print(np.__version__)

# 2. How to create a 1D array?
arr = np.arange(10)
arr

# 3. How to create a boolean array?

np.full((3, 3), True, dtype=bool)
np.full((3,3), '國字' , dtype=str)

# 4. How to extract items that satisfy a given condition from 1D array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_1 = arr[arr % 2 == 1]

# 5. How to replace items that satisfy a condition with another value in numpy array?Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Desired Output:
#>  array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# 如果他是奇數=-1如果是偶數=原本的數字
arr_1 = arr[arr % 2 == 1] = -1
arr_1

import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.where(arr % 2 == 1, -1, arr)

# 6. How to replace items that satisfy a condition without affecting the original array?
arr = np.arange(10)
a= np.where(arr%2 == 1,-1,arr)






