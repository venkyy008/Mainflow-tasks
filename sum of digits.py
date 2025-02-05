def getsum(num):
    sum=0
    for digit in str(num):
        sum+=int(digit)
    return sum
num=int(input("Enter a Number:"))
print(getsum(num))
