num = int(input("Number of rows and columns: "))
for i in range(1,num+1):
    for j in range(num-i):
            print("  ", end="")
    for g in range(2*i-1):
          print("* ",end="")
    print()