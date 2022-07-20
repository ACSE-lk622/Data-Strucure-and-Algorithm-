def ProductMax(nums):
    max = 0 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]*nums[j] > max :
                max = nums[i]*nums[j]
                pairs = str(nums[i]) + ',' + str(nums[j])

    print(pairs)
    print(max)

list = [2,534,676,223,445,123,664,233]
ProductMax(list)

def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
    num = []
    occur = []
    for i in range(len(arr)):
        if i not in num :
            num.append(arr[i])
            count = 0
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j] :
                    count+=1
                    occur.append(count)
        else :
            continue
    for i in range(len(occur)):
        if occur[i] not in occur[i+1:]:
            return True
        else :
            return False 

    print(occur)