def countSort(arr):
  count =[0 for i in range(256)]
  output=[0 for i in range(len(arr))]
  ans = ["" for _ in arr]

  for b in arr :
    count[ord(b)]+=1
  for i in range(len(arr):
    output[count[ord(arr[i])]-1]=arr[i]
    count[ord(arr[i])]-=1
  for i in range(len(arr)-1,0,-1):
     ans[i] = output[i]
  return ans            


