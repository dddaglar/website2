import sys, os
from PIL import Image

#grab first and second argument
curFol,newFol = sys.argv[1], sys.argv[2]

#check if folder exists , if not create second argument as a folder os.mkdir()
if not os.path.exists(newFol):
    os.mkdir(newFol)

#open the first argument file and read all the files inside of it
for samp  in os.listdir(curFol):
    f, e = os.path.splitext(samp)
    with Image.open(f"{curFol}{f}{e}","r") as im:
        im.save(f"{newFol}{f}.png")
