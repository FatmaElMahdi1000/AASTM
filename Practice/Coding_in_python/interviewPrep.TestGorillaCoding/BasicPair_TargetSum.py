def pairs_sums(MyList, target):
    nums = []
    for i in range(0, len(MyList)):
        for j in range(0, len(MyList)):
            if MyList[i] + MyList[j] == target and i != j:
                if MyList[i] not in nums and MyList[j] not in nums:
                    nums.append(MyList[i])
                    nums.append(MyList[j])
    if nums:
        return True

target = 10
MyList =  [4,7,1,9]
print(pairs_sums(MyList, target))