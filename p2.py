
count = 0
for i in range( 2, 100):
    flag = 1
    end = int(i** 0.5)+1
    for j in range( 2, end ):
       if i%j == 0:
        flag = 0
        break
    temp = 1
    end2 = int((i+2)** 0.5)+1
    for j in range( 2, end2 ):
       if (i+2) %j == 0:
          temp = 0

    if temp == 1 and flag == 1 : 
       count += 1
       if(count % 10 == 0):
             print("(",i,",",i+2,")", end = " ")
             print("\n")
       else:   
             print("(",i,",",i+2,")", end = " ")
            