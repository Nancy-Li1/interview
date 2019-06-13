#! /user/bin/python
# -*- coding:utf-8 -*-

'''
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2
输入：258
输出：2
输入：0219
输出：3
'''

def how_many_ways(digitarray):
    # implement here
    '''
    动态规划问题
    '''
    n = len(digitarray)
    if n == 0:
        return 0    
    if n == 1:
        return 1
    dp = [1]
    for i in range(1, length + 1):
        # if digitarray[i-1] == '0':
        #     dp.append(1)
        # else:
        dp.append(dp[i-1])
        if i>1 and (digitarray[i-2]=="1" or (digitarray[i-2]=="2" and digitarray[i-1]<="5")):
            dp[i] += dp[i-2]
    return dp[-1]
