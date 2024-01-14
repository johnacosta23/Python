# This is DMOJ problem dmopc15c7p2
# https://dmoj.ca/problems/?search=dmopc15c7p2

# The Challenge
# Calculate the volume of a right circular cone

# Hint: The formula to calculate the volume of a cone is (πr2h)/3.

# Pi will be defined as 3.1415

PI = 3.1415
radius = int(input())
height = int(input())
volume = ((PI)*(radius**2*height))/3
print("The volume of your cone is" + " " + str(volume))



# Remark : Good to say that if the user does not uses numbers for the radius annd height, the program will return an error, 
# It is not user-friendly at all, that’s for sure. But for purposes of learning to program, we won’t worry about this. 
