# Diamond pattern using nested loops

n = 4  # height of the pyramid

# Upper part
for i in range(0, n + 1):
    for j in range(0, i+1): #0 to i-1, first iteration (0,0) one star in that position, then (0:1) 2 stars
        print("*", end=" ") #end = " " printing stars side by side in the same line
    print() #before moving to the next i, we print like space,it just moves the cursor to a new line.

#lower part
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()