

def merge_sort(arr):

    n=len(arr)
    
    if n>1:
        left_arr=arr[:n//2]
        right_arr=arr[n//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=0
        j=0
        k=0

        while i< len(left_arr) and j<len(right_arr):
            
            if left_arr[i]<right_arr[j]:
           
                arr[k]=left_arr[i]
                i=i+1
           
            else:
           
                arr[k]=right_arr[j]
                j=j+1

            k=k+1


        while i<len(left_arr):
           
            arr[k]=left_arr[i]
           
            i=i+1
            k=k+1

        while j<len(right_arr):
           
            arr[k]=right_arr[j]
           
            j=j+1
            k=k+1


arr=[2,6,5,1,7,74,3]
merge_sort(arr) 
print(arr)