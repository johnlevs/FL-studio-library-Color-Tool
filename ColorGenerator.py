import colorsys
import pathlib
from pathlib import Path


##########################=HELPERS=#####################################
def RGB_to_hex(RGB):
    RGB = [int(x) for x in RGB]
    return "$"+"".join(["0{0:x}".format(v) if v < 16 else
        "{0:x}".format(v) for v in RGB])

def hex_to_rgb(hex):
    #backwards because fl is weird
    return [int(hex[4:6],16),int(hex[2:4],16),int(hex[0:2],16)]


###########################=MAIN SCRIPT=################################
# Declaring params
####################
black = 1
white = 1
top = 100.
bot = 180.
path = ""
c1 = "80ecff"
c2 = "8f80ff"
####################
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
            if hue:
                if words[0] == "BOTTOM:":
                    bot = float(words[1])
                elif words[0]=="TOP:":
                    top = float(words[1])
                elif words[0] == "LIGHT:":
                    white = float(words[1])/100.
                elif words[0] == "DARK:":
                    black = float(words[1])/100.
            elif grad:
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

if len(DirNames)==0:
    exit

if grad:    #gradient method
    RGB1 = hex_to_rgb(c1)
    RGB2 = hex_to_rgb(c2)
    D = ((RGB2[0]-RGB1[0])**2+(RGB2[1]-RGB1[1])**2+(RGB2[2]-RGB1[2])**2)**.5
    norm=[]
    for i in range(0,3): 
        norm.append((RGB2[i]-RGB1[i])/D)
    step = D/(len(DirNames)-1)
    for x in range(0,len(DirNames)):    
        d = step*(x)
        rgb_vect = [norm[i]*d+RGB1[i] for i in range(0,3)]
        #convert to Hex
        HexString = RGB_to_hex(rgb_vect)
        nfo_text = "Tip=Sorted packs of samples / patches\n\
        ' highlight this subdir\
        \nColor="+HexString+\
        "\nIconIndex=24 "
        with open(str(DirNames[x])+".NFO",'w') as file_object:
            file_object.write(nfo_text)
elif hue:
#hue range method
    if bot < 0  or top > 360 or\
        black*white>1 or black*white<0:
        print("invalid param file, check directions")
        exit

    # Generating NFO files
    slope = (top-bot)/360
    yIntcpt = bot/360
    for x in range(0,len(DirNames)):    
        hue = float(x/len(DirNames))*slope+yIntcpt
        #use HSV to cycle hues easily
        (r, g, b) = colorsys.hsv_to_rgb(hue, white, black)
        #convert to RGB
        rgb_vect = [ int(255 * b), int(255 * g),int(255 * r)]
        #convert to Hex
        HexString = RGB_to_hex(rgb_vect)

        nfo_text = "Tip=Sorted packs of samples / patches\n\
        ' highlight this subdir\
        \nColor="+HexString+\
        "\nIconIndex=24 "
        with open(str(DirNames[x])+".NFO",'w') as file_object:
            file_object.write(nfo_text)
