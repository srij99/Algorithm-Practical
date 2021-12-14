def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        MergeSort(left_arr)
        MergeSort(right_arr)

        i=j=k=0
        l=len(left_arr)
        r=len(right_arr)

        while i<l and j<r :
            if left_arr[i]<right_arr[j] :
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j += 1
            k+=1

        while i<l:
            arr[k]=left_arr[i]
            i+=1
            k+=1

        while j<r:
            arr[k]=right_arr[j]
            j+=1
            k+=1



if __name__ == "__main__":
    arr = [5,9,10,4,8,12,7]
    MergeSort(arr)
    print(arr,end=" ")