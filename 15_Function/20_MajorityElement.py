class Solution:
    def majorityElement(self, arr):
        count = 0
        cand = None
        
        for x in arr:
            if count ==0:
                cand = x
                count = 1
            elif x==cand:
                count +=1
            else:
                count -=1
                
        if arr.count(cand) > len(arr) // 2:
            return cand
            
        return -1