# enter number of row : 4
# 1

# 22

# 333

# 4444




n = eval(input("enter number of row : "))

for i in range( 1,n+1):
    for j in range(1, i+1):
             print(i , end="")
    print("\n")