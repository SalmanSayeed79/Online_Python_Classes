n=int(input("Enter your length : "))
if(n%2==0):
    print("Cannot make a diamond with even length")
else:
    upper_row=(int)((n+1)/2)   #3.1->3 3.9->3
    lower_row=(int)((n-1)/2)
    #diamond shape
    i=0
    while(i<upper_row):
        j=0
        while (j<=upper_row-1-i):
            print(" ",end="")
            j=j+1
        k=0
        while (k<=i):
            print("* ",end="")
            k=k+1
        print("")
        i=i+1


    i=0
    while(i<lower_row):
        j=0
        while (j<=i+1):
            print(" ",end="")
            j=j+1
        k=0
        while (k<=lower_row-1-i):
            print("* ",end="")
            k=k+1
        print("")
        i=i+1



# *
# **
# ***
# ****
# *****

#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 
# * * * * 
#  * * * 
#   * * 
#    * 