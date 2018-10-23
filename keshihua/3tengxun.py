def radix_sort(lst):
    bucket = [[], [], [], [], [], [], [], [], [], []]  # can not use [[]]*10
    bucket1 = [[], [], [], [], [], [], [], [], [], []]
    for i in lst:
        bucket[i % 10].append(i)
    lst1 = []
    for b in bucket:
        lst1.extend(b)
    for i in lst1:
        bucket1[i].append(i)
    lst2 = []
    for b in bucket1:
        lst2.extend(b)
    # print(lst2)
    return lst2


if __name__ == "__main__":
    line = input('Please input number:')
    l = []
    for i in line:
        l.append(int(i))
    l = radix_sort(l)
    for i in l:
        print(i, end='')
    # print(radix_sort(l))
