class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)  
        answer = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
    
        for i in count:
            buckets[count[i]] += [i]

        i = len(nums)
        while i > -1 and len(answer) < k:
            if buckets[i]:
                for j in range(len(buckets[i])):
                    if len(answer) < k:
                        answer.append(buckets[i][j])
            i -= 1
        return answer

