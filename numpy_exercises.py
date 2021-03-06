import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
len(a[a < 0])

# 2. How many positive numbers are there?
len(a[a > 0])

# 3. How many even positive numbers are there?
x = a[a > 0]
len(x[x % 2 == 0])

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
len(a[(a + 3) > 0])

# 5. If you squared each number, what would the new mean and standard deviation be?
b = a ** 2
np.mean(b)   # 74
round(np.std(b), 7) #144.0243035

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. 
#Center the data set. See this link for more on centering.
new_center =  np.mean(a)
a - int(new_center)

# 7. Calculate the z-score for each data point.
z_score = lambda x: (x - np.mean(a)) / np.std(a)
z_score(a)



import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)  # 55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a = product_of_a * num
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [number ** 2 for number in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [odds for odds in a if odds % 2 == 1]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [even for even in a if even % 2 == 0]
print(evens_in_a)



## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
bb = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b = bb.sum()    #with numpy


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = bb.min()    #with numpy


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = bb.max()    #with numpy

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = bb.mean()    #with numpy

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b = bb.prod()    #with numpy

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b = bb ** 2    #with numpy


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b = bb[bb % 2 == 1]    #with numpy


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b = bb[bb % 2 == 0]    #with numpy

# Exercise 9 - print out the shape of the array b.
bb.shape

# Exercise 10 - transpose the array b.
bb.transpose()

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
bb.reshape((1,6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
bb.reshape((6,1))



## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

cc = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
cc.min()
cc.max()
cc.sum()
cc.prod()

# Exercise 2 - Determine the standard deviation of c.
cc.std()

# Exercise 3 - Determine the variance of c.
cc.var()

# Exercise 4 - Print out the shape of the array c
cc.shape

# Exercise 5 - Transpose c and print out transposed result.
print(cc.transpose())

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(cc, cc)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(cc * cc.transpose()).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(cc * cc.transpose()).prod()



## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

dd = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(dd)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(dd)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(dd)

# Exercise 4 - Find all the negative numbers in d
dd[dd < 0]

# Exercise 5 - Find all the positive numbers in d
dd[dd > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(dd)

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(dd))

# Exercise 8 - Print out the shape of d.
dd.shape

# Exercise 9 - Transpose and then print out the shape of d.
print(dd.transpose())

# Exercise 10 - Reshape d into an array of 9 x 2
dd.reshape(9, 2)