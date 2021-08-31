# Index of element which is maximum element of row and minimum element of column
# [1, 2, 3],
# [1, 4, 9],
# [76, 34, 21]

# op row 1 col 3

def minMax(mat, r, c):
    for i in range(r):
        row_max=mat[i][0]
        row=-1
        col=-1
        for j in range(1, c):
            if mat[i][j] > row_max:
                row_max=mat[i][j]
                row=i
                col=j
        for k in range(0, c):
            if mat[k][col]< row_max:
                break
        if k+1==c:
            print(row+1, col+1)
            return True

    return False



row=3
col=3
mat=[[1, 2, 3],
        [1, 4, 9],
        [76, 34, 21]]
if not minMax(mat, row, col):
    print("No element found")


# time complexity = o(r*c)

