from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container_x = Counter(nums)
        frequent_k = container_x.most_common(k)
        answer = [x[0] for x in frequent_k] 
        return answer
