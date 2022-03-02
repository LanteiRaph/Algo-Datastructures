#Compile a class solution.
from pip import List


class Solution():
    #Brutal Force
    #Loop through each element x and chkc if x is the subtratction of the targe and anyother value
    def brutal(self,num:List[int],target:int ):
        #Loop through the num array and gt the ith value
        for i in range(len(num)):
            for j in range( i + 1, len(num)):
                if num[j] == target - num[i]:
                    return [i, j]


    #using hastables, key value mapping to maximaise on speed.
    #this approwch uses more space by less speed.
    def hashtable(self, nums:List[int], target:int) -> List[int]:
        #Create
        hashmap = {}

        #Loop through and check id the compliment exist if not add
        for i in range(len(nums)):
            #Subtract the i from the target
            complement = target - nums[i]
            #Check if compliment exist in the hashmaping
            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[nums[i]] = i