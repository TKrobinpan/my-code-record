import heapq


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy, experience):
        numene = sum(energy)-initialEnergy+1
        add_=0;j=0
        while j<len(experience):
            if initialExperience>experience[j]:
                initialExperience+=experience[j]
                j+=1
                
            else:
                add_+=experience[j]-initialExperience+1
                initialExperience+=add_
        return numene+add_


print(Solution().minNumberOfHours(5,3,[1,4,3,2],[2,6,3,1]))