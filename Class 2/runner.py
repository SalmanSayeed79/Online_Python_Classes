# Temp Converter degC to degF
print("=====================================")
print("Choose any of the options below:")
print("1. C to F")
print("2. F to C")
print("3. C to K")
print("4. K to C")
print("=====================================")
opt=input()

if(opt=="1"):
    c=float(input("Enter your Celcius temp : "))
    f=((c*9)/5)+32
    print("Your temp in F will be : ",f)
elif(opt=="2"):
    f=float(input("Enter your Farenheit temp : "))
    c=((f-32)/9)*5
    print("Your temp in C will be : ",c)
else:
    print("Please select a valid option!")

