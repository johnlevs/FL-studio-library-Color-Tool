import colorsys
import pathlib
from pathlib import Path

class Error(Exception):
    pass
class vectorsNotEqualLength(Error):
    pass
##########################=HELPERS=#####################################
def RGB_to_hex(RGB):
    RGB = [int(x) for x in RGB]
    return "$"+"".join(["0{0:x}".format(v) if v < 16 else
        "{0:x}".format(v) for v in RGB])

def hex_to_rgb(hex):
    #backwards because fl is weird
    return [int(hex[4:6],16),int(hex[2:4],16),int(hex[0:2],16)]



###########################=MAIN SCRIPT=################################
## READS PARAM FILE
with open("params.txt","r") as FO:
    fl = "".join(FO.readline().splitlines())
    hue = True if fl =="HUE" else False
    grad = True if fl =="GRADIENT" else False
    if not (hue or grad):
        print("Invalid Param file Header")
        exit
    for line in FO:
        words = line.split()
        if not len(words)==0:
            if words[0] == "DIRECTORY:":
                path = line.replace("DIRECTORY: ", "")
                path = path.replace("\n","")
            if words[0] == "OUTPUT:":
                outPath = line.replace("OUTPUT: ","")
                outPath = outPath.replace("\n","")
            if words[0] == "C1:":
                c1 = words[1]
            if words[0] == "C2:":
                c2 = words[1]     

p = Path(path)
if not p.exists:
    print("Invalid Path")
    exit
#counts directories
DirNames = []
for x in p.iterdir():
    if x.is_dir():
        DirNames.append(x)
resolution = len(DirNames)
if resolution==0:
    exit
RGB1 = hex_to_rgb(c1)
RGB2 = hex_to_rgb(c2)
if grad:
    vect1 = RGB1
    vect2 = RGB2
elif hue:
    vect1 = colorsys.rgb_to_hsv(RGB1[0]/255,RGB1[1]/255,RGB1[2]/255)
    vect2 = colorsys.rgb_to_hsv(RGB2[0]/255,RGB2[1]/255,RGB2[2]/255)



if len(vect1)!=len(vect2):
    raise vectorsNotEqualLength

# computes linear gradient between two vectors
D = ((vect2[0]-vect1[0])**2+(vect2[1]-vect1[1])**2+(vect2[2]-vect1[2])**2)**.5
step = D/(resolution-1)
norm = []
for i in range(0,len(vect1)):
    norm.append((vect2[i]-vect1[i])/D)
for x in range(0,resolution):  
    d = step*(x)
    pos = [norm[i]*d+vect1[i] for i in range(0,len(vect1))]
    HexString = ""
    if hue:
        #Converts back to RGB coordinates
        (r, g, b) = colorsys.hsv_to_rgb(pos[0], pos[1], pos[2])
        rgb_vect = [ int(255 * r), int(255 * g),int(255 * b)]
    else:
        rgb_vect = pos
    #converst to hex format
    HexString = RGB_to_hex(rgb_vect)
    nfo_text = "Tip=Sorted packs of samples / patches\n\
    ' highlight this subdir\
    \nColor="+HexString+\
    "\nIconIndex=24 "
    PrintPath = outPath+str(DirNames[x].parts[-1])+".NFO"
    with open(PrintPath,'w') as file_object:
        file_object.write(nfo_text)