#百鸡百钱
for x in range(1,21):
    for y in range(1,33):
        for z in range(1,100):
            if (x+y+z) == 100 and (x*5+y*3+z/3) == 100:
                print(x,y,z)