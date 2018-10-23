import sys


def chazhi(a, k):
    jia = 0
    jian = 0
    max = 0
    min = 0
    for i in range(a):
        i += k
        i -= k
        jia += i
        jian += i
        if max < jia:
            max = jia
        if min > jian:
            min = jian
    print(min, max)
    return max - min


if __name__ == "__main__":
    a = input('请输入a:')
    k = input('请输入k:')
    print(chazhi(int(a), int(k)))



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 判断是否为个位数，是个位数则不用反转，直接返回
        if -10 < x < 10:
            return x
        # 把整数x转为字符串
        str_x = str(x)
        # 判断第一个是否为负号
        if str_x[0] != "-":
            # 不是负号则直接反转
            str_x = str_x[::-1]
            # str转为int
            x = int(str_x)
        else:
            # 是负号，则反转负号之后的字符串
            str_x = str_x[1:][::-1]
            # str转int
            x = int(str_x)
            # 加上负号
            x = -x
        # 三目运算符，判断是否溢出
        # 如果-2147483648 < x < 2147483647则返回x，否则返回0
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    s = Solution()
    a = input()
    reverse_int = s.reverse(int(a))
    print(reverse_int)