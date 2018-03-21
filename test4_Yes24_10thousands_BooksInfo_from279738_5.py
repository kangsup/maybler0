with open("get_bookinfo_file2test.py", "w") as f:
    for i in range(10000):
        f.write('{}{}{}{}{}'.format("wget http://www.yes24.com/24/goods/", 279738+i, " -O sample", 279738+i, ".htm\n"))
    
