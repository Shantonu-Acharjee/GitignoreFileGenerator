import os


path = input("enter your path: ")
SZE = int(input("enter the size you want to separet: "))
file = open('fileDigger.txt','a+')



filelist = []

def wrt(text):
    file = open("fileDigger.txt", "w") 
    file.write(text) 
    file.close() 

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

for name in filelist:
    size = os.path.getsize(name)
    size = size/1000000
    #print("Path :",name,"|| SIZE :",str(float(size))+" MB")
    if size > 150:
        print("Path :",name,"|| SIZE :",str(float(size))+" MB")
        wrt(name)