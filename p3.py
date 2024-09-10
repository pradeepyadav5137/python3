count = 0

for i in range( 10,100000):
    n = i
    prime= 1
    end = int( n** 0.5)+1
    for j in range( 2, end ):
        if n%j == 0:
         prime = 0
         break
    if(prime == 1) :   
        
        num = 0
        temp = n
        while(temp>0):
            rem = temp%10
            num = (num * 10 ) + rem
            temp = temp//10
               # print(num)
        if num != i:
            flag = 1
            end = int( num ** 0.5)+1
            for j in range( 2, end ):
                if num%j == 0:
                 flag = 0
                 break
            if(flag == 1):  
                count += 1
                if (count >20):
                  break
                else:
                   if(count %10 == 0):
                      print( n , end =" ")
                      print("\n")
                   else:
                      print( n , end =" ")
                       
                                       
