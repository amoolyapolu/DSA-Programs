# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
matrix=[[1,1,1],[1,0,1],[1,1,1]]
m=[0]*len(matrix)
n=[0]*len(matrix[0])

#traverse the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            m[i]=1
            n[j]=1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if m[i] or n[j]:
            matrix[i][j]=0
print(matrix)
