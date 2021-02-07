from collections import Counter, deque
import heapq

class FreqWord(object):
    def __init__(self, word, occurence):
        self.word = word
        self.occurence = occurence

    def __lt__(self, other):
        if self.occurence == other.occurence:
            return lt(other.word, self.word)
        else:
            return lt(self.occurence, other.occurence)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:    
        counts = collections.Counter(words)
        max_heap = []
        for key, val in counts.items():
            heapq.heappush(max_heap,FreqWord(key, val))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = deque([]) # can also use a list and just reverse at the end
        while k > 0:
            res.appendleft(heapq.heappop(max_heap).word)
            k -= 1
        
        return list(res)
