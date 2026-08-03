#lzc = open("read.txt" ,"r" ,encoding='utf-8')
#json1 = open("./read.json" ,"r")
#print(json1.read())
#print(lzc.readlines())
#lzc.close()
#json1.close()

with open("read.txt" ,"r" ,encoding='utf-8') as lzc:
    print(lzc.read())