"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, one_str):
        define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if one_str=='0':
            return 0
        else:
            res=0
            for i in range(0,len(one_str)):
                if i==0 or define_dict[one_str[i]]<=define_dict[one_str[i-1]]:
                    res+=define_dict[one_str[i]]
                else:
                    res+=define_dict[one_str[i]]-2*define_dict[one_str[i-1]]
            return res
            # #下面这种写法也可以
            # for i in range(len(one_str)):
            #     if i > 0 and define_dict[one_str[i]] > define_dict[one_str[i - 1]]:
            #         res -= define_dict[one_str[i - 1]]
            #         res += define_dict[one_str[i]] - define_dict[one_str[i - 1]]
            #     else:
            #         res += define_dict[one_str[i]]
            # return res  