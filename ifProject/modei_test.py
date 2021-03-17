def mutiple_table():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            c = i * j
            print("%d * %d = %d\t" % (j, i, c),end="")
            j += 1
        print(end='\n')
        i += 1


mutiple_table()