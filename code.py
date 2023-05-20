
#                                    Divide The Apples

# Jethalal has got n number of apples,Jetha has some students among whom,he wants to distribute the apples.
# These n number of apples are provided to Jetha by his friend Taarak Mehta and he can request for few more or few less
# apples.You need to print whether a number in range mn to mx is divisor of n or not.

# Input:Take n,mx and mn from the user
# Output:Print whether the numbers between mn and mx are divisor of n or not.
# If mx=mn,then s.t this is not a range,and show the result for that number

n=int((input("Enter the no. of appples Jetha has got: ")))
mn=int(input("Enter minimum no. in range: "))
mx=int(input("Enter maximum no. in range: "))
list=[]
if mn==mx:
    print("This is not a range as minimum mad maximum are equal!")
    if n % mn == 0:
        print(f"{n} is divisor of {mn}")
    else:
        print(f"{n} is not a divisor of {mn}")

else:
    for i in range(mn,mx+1):
            if n%i==0:
               print(f"{i} is divisor of {n}")
            elif (n%i)!=0:
                print(f"{i} is not a  divisor of {n}")







