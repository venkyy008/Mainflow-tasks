def reverse_list(lst):
    """Reevrse a list in-place."""
    start=0
    end=len(lst)-1
    while start < end:
        lst[start], lst[end]=lst[end],lst[start]
        start+=1
        end-=1
        return lst
my_list=[1,2,3,4,5]
print(reverse_list(my_list))
