class Solution:
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        final_list = []
        for i in sorted_intervals:
            currentInterval = i
            if final_list:
                if final_list[-1][1] >= i[0]: 
                    currentInterval = final_list.pop()
                    if i[1] > currentInterval[1]:
                        currentInterval[1] = i[1]      
            final_list.append(currentInterval)
        return final_list
