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
np.count_nonzero(a + 3 > 0)

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