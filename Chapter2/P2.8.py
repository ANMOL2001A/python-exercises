import math 
width =float(input("enter heights of rectangle:"))
height=float(input("enter width of rectangle:"))
 # perameter of rectangle 2(height+width)
perameter = 2 * (height+width)
print(f"Perameter is: {perameter}")
# formula of diagonal length of rectangle  
diagonal_length = math.sqrt((height**2) + (width**2))
print(f"diagonal length is : {diagonal_length}")