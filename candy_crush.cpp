arr=[4, 4, 5, 5, 5, 7, 7, 1]
op expected: 4 4 7 7 1

c = 1
prev=arr[0]
i=1
while i < len(arr):
    if arr[i]!=prev:
        c=1
        prev=arr[i]
    else:
        c+=1
    if c>=3:
        arr=arr[:i-2]+arr[i+1:]
        i=i-3
    i+=1
print(arr)
