"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <10:
            return n
        length = len(str(n))
        t = n
        for i in xrange(0,length):
            temp = 9*pow(10,i)*(i+1)

            if t > temp:
                t-=temp
            elif t == temp:
                return 9
            elif t < temp:
                if t % (i+1)==0:
                    #print pow(10,i)+ t/(i+1)-1
                    di = str(pow(10,i)+ t/(i+1)-1)[-1]
                else:
                    di = str(pow(10,i)+t/(i+1))[t % (i+1)-1]
                return int(di)
A = Solution()
print A.findNthDigit(184)