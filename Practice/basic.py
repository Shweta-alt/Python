# first program in python 

print('hello am here!')


# second program 

# Problem: 
# Today is a holiday at the children's camp, so all the children will be served ice cream.
# There are 68 children in the group, and each child should get 2 scoops of ice cream.

# Task
# Write a program to calculate and output the total number of ice cream scoops we need.


n = 68
i = 2

scoops = n*i
print(scoops)



# Calculate and output the number of miles in 1000 kilometers.

# Hint
# One mile is 1.6 kilometers, so find the quotient of 1000 and 1.6.
# hint: Use the floor division operator //.


one_miles = 1.6
miles = 1000

quotient = miles // one_miles
print(quotient)



# Exponentiation


# Exponentiation is the raising of one number to the power of another.
# This operation is performed using two asterisks **.

# Let's use exponentiation to solve a known problem.
# You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).

# Task:
# Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.

# Hint:
# Let's see how exponentiation can be useful to perform the calculation.
# For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).
# Use the print statement to output the resulting amount.
# PY


expo_num = 0.01*(2**30)
print(expo_num)
