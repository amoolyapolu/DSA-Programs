# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
matrix=[[1,1,1],[1,0,1],[1,1,1]]
def matrixRow(matrix,i):
    for j in range(len(matrix)):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
def matrixCoulmn(matrix,j):
    for i in range(len(matrix[0])):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
for i in range(len(matrix)):
    print(i)
    for j in range(len(matrix[0])):
        print(j)
        if matrix[i][j]==0:
            matrixRow(matrix,i)
            
            matrixCoulmn(matrix,j)
            
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==-1:
            matrix[i][j]=0
for i in range(len(matrix)):
    print(matrix[i])
          
