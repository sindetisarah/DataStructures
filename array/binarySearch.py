def binarySearch(list,target):
    found = False
    low = 0
    high = len(list)-1
    while low <= high and not found:
        mid = (low+high) // 2
        if list[mid] == target :
            found == True
        elif target > list[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("Target is found")
    else:
        print("Target not found")
list = [1,2,4,78,5]
list.sort()
target = int(input("Please input your targert:"))
binarySearch(list, target)


    
