n = int(input())
arr = map(int, input().split())
set_list = set()
for number in arr:
    set_list.add(number)

print(sorted(set_list)[-2])