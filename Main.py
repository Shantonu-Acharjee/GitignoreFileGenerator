#1.jpg, 2.mp4, 3.txt, 4.jpg
import os
size = os.stat("1.jpg").st_size
#size = size / 1024
print(size,'MB')