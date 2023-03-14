def mergeSort(rangeList):
   if len(rangeList)>1 :
        midPoint = len(originalList) // 2
        left_list = originalList[ :midPoint]
        right_list = originalList[midPoint: ]
        mergeSort(left_list)
        mergeSort(right_list)
        pickL = 0
        pickR = 0
        appendE = 0
   while pickL<len(left_list) and pickR<len(right_list):
        if left_list[pickL] < right_list[pickR]:
            rangeList[appendE] = left_list[pickL]
            pickL = pickL+1
            appendE = appendE+1
        else:
            rangeList[appendE] = right_list[pickR]
            pickR = pickR+1
            appendE = appendE+1
   while pickL<left_list:
        rangeList[appendE] = left_list[pickL]
        pickL = pickL+1
        appendE = appendE+1
   while pickR<left_list:
        rangeList[appendE] = right_list[pickR]
        pickR = pickR+1
        appendE = appendE+1

originalList = [1,45,67,89,12,34]
rangeList = [originalList for num in range(len(originalList))]
mergeSort(rangeList)
print(rangeList)