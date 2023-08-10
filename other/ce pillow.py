#!/usr/bin/env python3
import os,sys
from PIL import Image

size=(128,128)

for infile in os.listdir():
    outfile=os.path.splitext(infile)[0]
    try:
        with Image.open(infile).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("/opt/icons/"+outfile,"JPEG")
    except OSError:
        pass

#---alt code
# #!/usr/bin/env python3

# import os, glob
# from PIL import Image

# newsize = 128, 128

# for file in glob.glob("ic_*"):
#        im = Image.open(file).convert('RGB')
#        im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")


