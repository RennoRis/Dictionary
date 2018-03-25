data = {"Jane Doe":"+27 555 5367" , "John Smith":"+27 555 6254" , "Bob Stone":"+27 555 5689"}
data ["Jane Doe"] = "+27 555 1024"
data.update({"Anna Cooper" : "+27 555 3237"})
print (data ['Jane Doe'])
print (data ['Anna Cooper'])
print (data ["Bob Stone"])
print (" ")
print (" ")
print (" ")
print ("Semua Data : ")
for key, val in data.items():
    print(key, val)
print (" ")
print (" ")
print (" ")
print ("Semua Value : ")
for value in data:
    print(data[value])
