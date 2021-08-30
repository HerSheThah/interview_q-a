# 5       1 

#   4   2   

#     3     

#   2   4   

# 1       5 


n=5
for i in range(n):
    if i <= n//2:
        for j in range(n, 0, -1):
            if j == i+1 or j == (n-i):
            #  print(i, j, "ij", end="        ")
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print("\n")
    else:
        for j in range(1, n+1):
            if j == i+1 or j == (n-i):
            #  print(i, j, "ij", end="        ")
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print("\n")
