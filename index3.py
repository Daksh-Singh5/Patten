num = int(input("Number of rows and columns: "))
g=0
for i in range(num):
    for j in range(i+1):
            print(g, end="|")
            g+=1
    print()