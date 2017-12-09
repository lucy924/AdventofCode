"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23 ---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 325489.

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25 ---> ...

"""

# First step find which ring it is in (1x1, 3x3, 5x5)
# Second step find position in the ring
# Third step find how far away it is from the centre (x,y - x,y = difference = no.of steps)

from math import sqrt

# Example using number 24
number = 24

# First Step: find which ring it is in
right_ring = 0  #initialising the variable which will contain the ring number (1, 3, 5, 7 etc)
ring = 1    #starting calculations at ring 1 (just 1 digit in centre)
while right_ring == 0:      #keeps loop going until right_ring is found
    corner1 = ring ** 2     #ring number squared = the number in bottom right corner, the end of the ring
    corner2 = (ring + 2) ** 2   #the next ring corner
    if corner1 < number <= corner2: #The number will be a digit in between the two corners
        right_ring = int(sqrt(corner2))     #right_ring number stored as a single digit, not the corner number
    else:
        ring = ring + 2     #keeps loop going through the rings until right_ring is found

print(right_ring)

#Second Step: find position in the ring
ring_list = []  #initialises a list for the numbers in the ring
for i in range(corner1 + 1, corner2 + 1):   #loops through the numbers in the ring, making a list of them
    ring_list.append(i)
print(ring_list)

for index in range(0, len(ring_list)):  #accesses each index of the numbers in ring_list
    if number == ring_list[index]:      #checks which index matches the number
        position = index + 1       #index + 1 is the physical position in the list, taking into account indexing from 0
print (position)

#comments all relate to 5x5 grid
#if right_ring = 5, then there are 5 rows and 5 columns
side = int(position / (right_ring - 1))  # 0 = column 4 (y = 4), 1 means row 0 (x = 0), 2 means column 0 (y = 0), 3 means row 4 (x = 0)
pos = int(position % (right_ring - 1))   # 0 = index 0, 1 = index 1, 2 = index 2, 3 = index 3

print(side)
print(pos)

if side == 0:
    y = 4
    if pos == 0:
        x = 3
    elif pos == 1:
        x = 2
elif side == 1:
    x = 0
    if pos == 0


#Third Step: find how far away it is from the centre (x,y - x,y = difference = no.of steps)

