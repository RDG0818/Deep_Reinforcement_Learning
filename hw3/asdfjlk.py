my_dict2 = {}
for i in range(60):
    step_num = input()
    temp = step_num.split("\t")
    my_dict2[int(temp[0])] = float(temp[1])

print(my_dict2)