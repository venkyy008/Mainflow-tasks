original_list=[1,2,2,3,4,4,5,6,5]
unique_list=[]
[unique_list.append(x) for x in original_list if x not in unique_list]
print(unique_list)
