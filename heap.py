def maxHeapify(A,n, i) :
  l=2i
  r=2i+1
  if l< n and A[l]>A[r] : 
    largest=l
  else: largest=i
  if r<n and A[r]>A[largest] :
    largest=r
  else : largest=i
  if largest!= i :
    a=A[largest]
    b=A[i]
    A[largest]=b
    A[i]=a
    maxHeapify(A,n,largest)
    
def buildMaxHeap(A) :
  l=len(A)//2
  i=0
  while(i<=l):
    maxHeapify(A,l,i)
    i=i+1
 
  
def heapSort(A) :
  buildMaxHeap(A)
  for l in range(len(A)-1,0,-1) :
    a=A[l]
    b=A[0]
    A[l]=b
    A[0]=a
    maxHeapify(A,l,0)
  
  
  
  
  
  
  
  
  
  
 
