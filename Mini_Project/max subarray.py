
   
import sys

def maxCrossingSum(arr, l ,mid,r):

    sum =0
    left_sum = -sys.maxsize
    for i in range(mid,l-1,-1):
        sum = sum + arr[i]
        if sum>left_sum:
            left_sum = sum

    sum = 0
    right_sum = - sys.maxsize
    for i in range(mid+1,r+1):
        sum = sum + arr[i]
        if sum>right_sum:
            right_sum = sum

    return max(left_sum+right_sum,left_sum,right_sum)

def maxSumSubarray(arr,l,r):
    if l==r:
        return arr[l]
    mid = (l+r)//2
    return max(maxSumSubarray(arr,l,mid),maxSumSubarray(arr,mid+1,r),maxCrossingSum(arr,l,mid,r))

if __name__ == "__main__":
    arr = [3,7,-4,1,-8,2,5,0,9,-6]
    N = len(arr)-1
    maxsum = maxSumSubarray(arr,0,N)
    print(maxsum)
