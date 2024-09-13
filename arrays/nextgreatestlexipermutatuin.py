def nextGreaterPermutation(A):
  #find the index in which we can swap the element
  index = -1
  for i in range(n-2,-1,-1):
    if A[i]<A[i+1]:
      index = i
      break
  #we dont find the break condition,so we reverese the array
  if index == -1:
    A.reverse()
    break
  #find the index and look for the value to be replaced
  for i in range(n-1,index,-1):
    if A[i]>A[index+1]:
      A[i],A[index]=A[index],A[i]
      break
  #swap the elements post index to form next lexicographically possibel
  A[index+1:] = reversed(A[i+1:])
A = [2, 1, 5, 4, 3, 0, 0]
ans = nextGreaterPermutation(A)
