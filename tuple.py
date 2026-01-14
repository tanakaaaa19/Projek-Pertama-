# membuat list
myList = [1,True, "Ok"]
myList.append(100)
print(myList)


# Tuple
myTuple = (1,True,"Oke")
# myTuple.append(100)
print(myTuple)

# menambahkan data tuple dg operator + dan *
# menggabung tuple
gabungTuple = myTuple + (10,20,30)
print(gabungTuple)

# gandakan isi tuple
gandakanTuple = gabungTuple * 2
print(gandakanTuple)

# akses tuple
print(gabungTuple[2])
print(gabungTuple[-2])

# akses tuple melalui for
for data in gabungTuple:
    print("Data didalam tuple:", data)
    
# nested tuple
myNestedTuple = ("Aku", "suka", "makan", ("apel", "pisang", "stroberi"))
print(myNestedTuple[0], myNestedTuple[2],myNestedTuple[-1][2])