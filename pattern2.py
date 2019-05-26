num = 5
space = num -1
star = num - space
for i in range(num):
    for j in range(space):
        print(" ",end="")
    for k in range(star):
        print("* ",end="")
    star=star+1
    space=space -1
    print("")
star = num-1
space = num - star
for i in range(num-1):
    for j in range(space):
        print(" ",end="")
    for k in range(star):
        print("* ",end="")
    space = space + 1
    star = star -1
    print("")