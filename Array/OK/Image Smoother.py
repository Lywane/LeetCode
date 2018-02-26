# -*- coding: utf-8 -*-
"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

"""
"""
蠢!!!
"""
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        N = []
        lenM = len(M)
        lenm = len(M[0])
        if lenm == 1 and lenM==1:
            return M
        elif lenm!=1 and lenM == 1:
            N.append([])
            for i in range(lenm):
                if i == 0:
                    N[0].append((M[0][i]+M[0][1])/2)
                elif i == lenm -1:
                    N[0].append((M[0][lenm -1]+M[0][lenm -2])/2)
                elif 0<i<lenm-1:
                    N[0].append((M[0][i]+M[0][i-1]+M[0][i+1])/3)
            return N
        elif lenm == 1 and lenM!=1:
            for i in range(lenM):
                N.append([])
                if i == 0:
                    N[i].append((M[i][0]+M[i+1][0])/2)
                elif i == lenM-1:
                    N[i].append((M[i][0]+M[i-1][0])/2)
                elif 0<i<lenM-1:
                    N[i].append((M[i-1][0]+M[i][0]+M[i+1][0])/3)
            return N
        for i in range(lenM):
            N.append([])
            if i == 0:
                for j in range(lenm):
                    if j == 0:
                        N[i].append((M[0][1]+M[1][0]+M[0][0]+M[1][1])/4)
                    elif 0 < j < lenm-1:
                        N[i].append((M[0][j]+M[0][j+1]+M[0][j-1]+M[1][j]+M[1][j-1]+M[1][j+1])/6)
                    elif j == lenm-1:
                        N[i].append((M[0][lenm-1] + M[1][lenm-1] + M[0][lenm-2]+M[1][lenm-2]) / 4)
            elif 0<i<lenM-1:
                for j in range(lenm):
                    if j == 0:
                        N[i].append((M[i][0]+M[i-1][0]+M[i+1][0]+M[i][1]+M[i+1][1]+M[i-1][1])/6)
                    elif 0 < j < lenm - 1:
                        N[i].append((M[i][j]+M[i+1][j]+M[i-1][j]+M[i][j-1]+M[i+1][j-1]+M[i-1][j-1]+M[i][j+1]+M[i-1][j+1]+M[i+1][j+1])/9)
                    elif j == lenm - 1:
                        N[i].append((M[i][lenm-1] + M[i - 1][lenm-1] + M[i + 1][lenm-1] + M[i][lenm-2] + M[i + 1][lenm-2] + M[i - 1][lenm-2]) / 6)
            elif i == lenM - 1:
                for j in range(lenm):
                    if j == 0:
                        N[i].append((M[lenM - 1][1] + M[lenM - 2][0] + M[lenM - 1][0] + M[lenM - 2][1]) / 4)
                    elif 0 < j <lenm-1:
                        N[i].append((M[lenM - 1][j] + M[lenM - 1][j + 1] + M[lenM - 1][j - 1] + M[lenM - 2][j] + M[lenM - 2][j - 1] + M[lenM - 2][j + 1]) / 6)
                    elif j == lenm - 1:
                        N[i].append((M[lenM - 1][lenm - 1] + M[lenM - 1][lenm - 2] + M[lenM - 2][lenm - 1] + M[lenM - 2][lenm - 2]) / 4)
        return N

A = Solution()
print A.imageSmoother([[2,5],[8,4],[0,1]])