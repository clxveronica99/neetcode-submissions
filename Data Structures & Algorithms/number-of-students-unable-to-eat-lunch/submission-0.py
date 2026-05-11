import collections
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = collections.Counter(students)
        cir, squ = counter[0], counter[1]
        for sand in sandwiches:
            if sand == 0 and cir == 0:
                return squ
            
            if sand == 1 and squ == 0:
                return cir
            
            if sand == 0:
                cir -= 1
            else:
                squ -= 1
        return 0    