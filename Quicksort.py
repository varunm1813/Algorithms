#python program to do quicksort

def quicksort(A,start,end):
  if start<end:
    pindex = partition(A,start, end)
    quicksort(A,start,pindex-1)
    quicksort(A,pindex+1,end)
  return A

def partition(A,start,end):
  pindex = start
  pivot = A[end]
  print(pivot)

  for i in range(start,end):
    if A[i]<=pivot:
      A[pindex],A[i] = A[i], A[pindex]
      pindex = pindex+1
  A[pindex], A[end] = A[end],A[pindex]
  return pindex

A=[3,4,7,5,8,10,56,7,0,1,4,6,4,34]
print(quicksort(A,start=0,end=len(A)-1))









