import os


path = input("enter your path: ")
SZE = int(input("enter the size you want to separet: "))
file = open('fileDigger.txt','a+')

#SZE = 1
#path ="/mnt/sda1/Books"

filelist = []
z = " "
i = 0

def wrt(text):
    file = open("fileDigger.txt", "w") 
    file.write(text) 
    file.close() 

for root, dirs, files in os.walk(path):
	for file in files:
                
		filelist.append(os.path.join(root,file))

for name in filelist:
    size = os.path.getsize(name)
    size = size/1000000
    #print("Path :",name,"|| SIZE :",str(float(size))+" MB")
    if size > SZE:
        i += 1
        print("Path :",name,"|| SIZE :",str(float(size))+" MB")
        #wrt(name)
        z += "   "
        z += str(i)
        z += "-----"
        z += name
#print(z)
wrt(z)