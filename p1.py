 
count = 0

for i in range( 1000,10000):
    num = 0
    n = i
    while(n>0):
        rem = n%10
        num = (num * 10 ) + rem
        n = n//10

    if num == i:
           count += 1
           if count >=10:
            print(i , end=" ")
            print("\n")
            count = 0  
           else: 
            print(i , end=" ")
           
