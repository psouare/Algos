def partition(A,p,r):
  pivot=A[r]
  i=p-1
  for j in range(p,r-1,1):
    if(A[j]<=pivot):
      i=i+1
      A[j],A[i]=A[i],A[j]
  A[r],A[i+1]=A[i+1],A[r]
  return i+1
def quicksort(A,p,r) :
  if(p<r):
    q=partition(A,p,r)
    quicksort(A,p,q-1)
    quicksort(A,p,q+1)







