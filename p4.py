count = 0

for i in range( 2,1000000):
    num = 0
    n = i
    while(n>0):
        rem = n%10
        num = (num * 10 ) + rem
        n = n//10

    if num == i:  
           flag = 1        
           end = int(num** 0.5)+1
           for j in range( 2, end ):
              if num%j == 0:
                 flag = 0
                 break
              
           if( flag == 1):
               count += 1
    
               if(count <= 100):
                  if(count % 10 == 0):
                      print( num , end=" ")   
                      print("\n")
                  else:
                    print( num , end=" ")  