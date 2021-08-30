
# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.

arr= [1,2,3,7,5]
s=12
def subArraySum(arr, s):
    cur_sum=arr[0]
    start=0
    end=1
    while end<=len(arr):
        if cur_sum==s:
            print([start+1, end])
            return
        if cur_sum>s and start<end:
            cur_sum -= arr[start]
            start+=1
        elif cur_sum<s and end<len(arr):
            cur_sum+= arr[end]
            end+=1


subArraySum(arr, s)
