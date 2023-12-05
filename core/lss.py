def largesmallsumm(arr):
    arr.sort()
    print(arr)
    if(arr is False):
        return 0
    smallest = arr[3]
    largest = 0
    if (len(arr)-1)%2==0:
        largest = arr[len(arr)-3]
    else:
        largest = arr[len(arr)-4]
    return (largest,smallest)
    
    
    
    
arr = [3,2,1,7,5,4,8,6]
print(largesmallsumm(arr))

