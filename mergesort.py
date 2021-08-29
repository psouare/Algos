def mergesort(arr):
  if(len(arr)>1):
    mid=len(arr)//2
    R=arr[mid:]
    L=arr[:mid]
    
    mergesort(R)
    mergesort(L)
    i=j=k=0
    
    while(i<len(L) and j<len(R)):
      if L[i] < R[i] :
        arr[k]=L[i]
        i+=1
      else :
        arr[k]=R[j]
        j+=1
      k+=1
        
     while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
 
     while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
      
  



