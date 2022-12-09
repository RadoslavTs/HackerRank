N = int(input())
my_list = []
for sequence in range(N):
    input_command = input().split()
    if input_command[0] == "insert":
        number = int(input_command[2])
        index = int(input_command[1])
        my_list.insert(index, number)
    elif input_command[0] == "print":
        print(my_list)
    elif input_command[0] == "remove":
        number = int(input_command[1])
        my_list.remove(number)
    elif input_command[0] == "append":
        number = int(input_command[1])
        my_list.append(number)
    elif input_command[0] == "sort":
        my_list = sorted(my_list)
    elif input_command[0] == "pop":
        my_list.pop()
    elif input_command[0] == "reverse":
        my_list.reverse()
