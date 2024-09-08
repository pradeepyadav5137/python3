

n = eval(input("enter number of row : "))

for i in range( 0 , n ):
     for j in range ( n, n-i-1,-1):
          print(j , end=" ")
     print( "\n")