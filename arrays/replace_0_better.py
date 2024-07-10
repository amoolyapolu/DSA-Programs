# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

"""

We start by doing an inplace replacement, first we do first row and first column, since [0,0] is an overlap position, 
we use an extra variable rowZero to keep track of value, and then go with the remaining elements in the first row and first column
if any of the value in the matrix for thsoe is zero we mark all the colummn values to zero but for row wise marking make sure we dont consider
column=0 since we already have a rowZero inplace.

Next we move to the next set of row and column and if either of the row or column value is zero we mark all the elements of that row and 
column to zero.

If matrix[0][0] =0 then , we try to make all elements of first row  to zero
if rowZero =0 , then we try to make all elements of first column to zero

""""

r=len(matrix)
c=len(matrix[0])
rowZero=False
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            
            matrix[0][j]=0
            if j>0:
                matrix[i][0]=0
            else:
                rowZero=True
    
for i in range(1,r):
    for j in range(1,c):
        if matrix[i][0]==0 or matrix[0][j] == 0 :
            matrix[i][j]=0

if matrix[0][0]==0:
    for j in range(c):
        matrix[0][j]=0

        
if rowZero:
    for i in range(r):
        matrix[i][0]=0
print(matrix)


""" Another approach https://www.youtube.com/watch?v=dSxt3ZCbIqA """
