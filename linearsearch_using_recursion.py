def linear(arr,n,key):
    if n==0:
        return n

    linear(arr,n-1,key)
    if arr[n-1]==key:
        print(n-1)
arr=[1,2,3,4,5,6,7]
n=len(arr)
key=5
linear(arr,n,key)