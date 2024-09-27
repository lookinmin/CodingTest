class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x : (x[0], -x[1]), reverse=True)

        q = []
        for val in people:
            q = q[:val[1]] + [val] + q[val[1]:]
        
        return q