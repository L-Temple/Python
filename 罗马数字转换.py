chart = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
strs = input()
result = 0
omit = -1  # omit为需省略的字符位
if strs in chart:
    print(chart[strs])
else:
    for i in range(len(strs)):  # 遍历字符串的每一位:(0,len-1)
        if i == omit:  # 如果无需省略i
            pass
        elif i <= len(strs) - 2:  # 如果还没有遍历到最后一位:(len-1-1)
            if chart[strs[i]] < chart[strs[i + 1]]:  # 如果前一位对应值小于后一位的
                result += chart[strs[i + 1]] - chart[strs[i]]  # 进行减操作
                omit = i + 1  # 省略下一位字符
            else:
                result += chart[strs[i]]
        else:  # 遍历到最后一位
            result += chart[strs[i]]
    print(result)