arr = [12, -3, 7, 0, 25, 18, -10, 5, 42, 7, 3, 99, -1,5]
# for even positions
for x in range(len(arr)//2):
  print(arr[x*2])

#if list is odd
if len(arr)%2==1:
  print(arr[-1])

# for odd positions
for x in range(len(arr)//2):
  print(arr[x*2+1])

