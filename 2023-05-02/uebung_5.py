# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

previous_i = 0

for i in range(10):
    sum = i + previous_i
    print(f"Current Number {i} Previous Number  {previous_i}  Sum:  {sum}")
    previous_i = i
