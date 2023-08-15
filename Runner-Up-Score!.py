n = int(input())
arr = map(int, input().split())

sort_arr = sorted(list(arr))
empty_list = []
for i in sort_arr:
    if i not in empty_list:
        empty_list.append(i)
print(sort_arr[-2])