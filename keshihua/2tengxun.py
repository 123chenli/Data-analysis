n, l = map(int, input().split(' '))
p = [int(x) for x in input().split(' ')]
# 最长路径搜索
node_len = [0] * n
node_len[0] = 1
for i in range(n - 1):
    node_len[i + 1] = node_len[p[i]] + 1

# 最长路径
max_len = max(node_len)
if max_len - 1 > l:
    print(l + 1)
else:
    residuce = l - max_len + 1
    residuce_len = int(residuce / 2)
    print(min(n, max_len + residuce_len))