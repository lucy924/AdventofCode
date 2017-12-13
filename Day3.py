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
from math import fabs

# Example using number 24
number = 325489
print ("Number used: ", number)

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

print("Ring number, (eg. 5 means ring 5x5): ", right_ring)
ring_coord = right_ring - 1

#Second Step: find position in the ring
ring_list = []  #initialises a list for the numbers in the ring
for i in range(corner1 + 1, corner2 + 1):   #loops through the numbers in the ring, making a list of them
    ring_list.append(i)
#print("The ring list: ", ring_list)

for index in range(0, len(ring_list)):  #accesses each index of the numbers in ring_list
    if number == ring_list[index]:      #checks which index matches the number
        position = index       #index position in the list, indexing from 0
        break
print ("Index position of number in the ring: ", position)

#comments all relate to 5x5 grid
#if right_ring = 5, then there are 5 rows and 5 columns, we treat all sides as a list of 4 values (ring_coord)
side = int(position / ring_coord)  # 0 = column 4 (y = 4), 1 means row 0 (x = 0), 2 means column 0 (y = 0), 3 means row 4 (x = 0)
side_pos = int(position % (ring_coord))   # 0 = index 0, 1 = index 1, 2 = index 2, 3 = index 3

last_col = 0
last_row = 3
row_0 = 1
col_0 = 2

last_col_coord = ring_coord
last_row_coord = ring_coord
row_0_coord = 0
col_0_coord = 0
sides = [row_0, last_row, col_0, last_col]

#last column and first row count up but backwards, so need to reverse index numbers to find coordinates. (Done by: total number of values in the list MINUS each value)
#position needs to add 1 to index value because we are beginning our count 1 position after the corner
if side is last_col:
    row = ring_coord - (side_pos + 1)
    col = last_col_coord
elif side is col_0:
    row = side_pos + 1
    col = col_0_coord
elif side is row_0:
    col = ring_coord - (side_pos + 1)
    row = row_0_coord
else:
    col = side_pos + 1
    row = last_row_coord

print ("Co-ordinates are: ", (row, col))


#Third Step: find how far away it is from the centre (x,y - x,y = difference = no.of steps)

centre_row = ring_coord/2
centre_col = ring_coord/2
dif_row = fabs(row - centre_row)
dif_col = fabs(col - centre_row)
steps = dif_col + dif_row

print("Number of steps: ", steps)

"""
Output:
Number used:  325489
Ring number, (eg. 5 means ring 5x5):  571
Index position of number in the ring:  1727
Co-ordinates are:  (570, 18)
Number of steps:  552.0

Your puzzle answer was 552.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 325489.

"""