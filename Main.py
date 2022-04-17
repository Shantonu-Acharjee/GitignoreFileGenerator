import os
PhotoDir = (input('Enter Your Folder Path : ')+ '/')
Photos = os.listdir(PhotoDir)
a = len(Photos)






for i in range(0, a):
    #print(Photos[i])
    size = os.stat(PhotoDir+Photos[i]).st_size
    size = size / 1000000
    print(size,'MB')
    if size >= 145:
        try:
            old_name = PhotoDir+Photos[i]
            new_name = PhotoDir+"GitIgnore."+Photos[i]
            os.rename(old_name, new_name)
        except:
            print('Rename Not Done.....!')

