import os
from pathlib import Path


a = os.listdir()
FirstList = []

f =  open('.gitignore', 'w') 


def FileSize(FilePath):
    file_size = int(os.path.getsize(FilePath))
    file_size = file_size / 1000000
    if file_size >= 20:
        f.write(FilePath+'\n')

    
for i in range(0, len(a)):

    if a[i] == 'Main.py':
        continue

    elif a[i] == '.gitignore':
        continue

    elif Path(f'{a[i].lower()}').suffix == '.py' :
        pass


    elif Path(f'{a[i].lower()}').suffix == '.mp3' :
        pass



    elif Path(f'{a[i].lower()}').suffix == '.mp4' :
        FileSize(a[i])


    elif Path(f'{a[i].lower()}').suffix == '.png' :
        pass


    elif Path(f'{a[i].lower()}').suffix == '.jpg' :
       pass


    elif Path(f'{a[i].lower()}').suffix == '.txt' :
       pass






    else:
        FirstList.append(a[i])
print(FirstList)
        
    

for i in range(0, len(FirstList)):
    pass
    


