"""
Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals
the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the
range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = points
        zhong = []
        for i in range(length):
            for j in range(i,length):
                x1=points[i][0]
                x2=points[j][0]
                y1=points[i][1]
                y2=points[j][1]
                if x1==x2:
                    zhong.append({'k':0,'b':(y1+y2)/2})
                elif y1==y2:
                    zhong.append({'x':(x1+x2)/2})
                else:
                    zhong.append({'k':(x1-x2)/(y2-y1),'b':(y2*y2-y1*y1)/(x1*x1-x2*x2)/2})
        print zhong

A = Solution()
A.numberOfBoomerangs([[0,1],[2,1]])

