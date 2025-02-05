def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(x,y):
    return(x*y)//gcd(x,y)
num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:"))
print("The GCD of",num1,"and",num2,"is",gcd(num1,num2))
print("The LCM of",num1,"and",num2,"is",lcm(num1,num2))
