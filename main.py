import os
import os.path
import fnmatch

path = input("Enter the path to root A32NX liveries folder: ")

for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames if fnmatch.fnmatch(f, 'texture.cfg')]:
        try:
            with open(os.path.join(dirpath, filename), 'w') as file:
                file.write("[fltsim]\n\nfallback.1=..\..\FlyByWire_A320_NEO\TEXTURE\nfallback.2=..\..\..\..\\texture\DetailMap\nfallback.3=..\..\..\..\\texture\Glass\nfallback.4=..\..\..\..\\texture\Interiors\nfallback.5=..\..\..\..\\texture\nfallback.6=..\\texture")
            print("Converted " + dirpath + filename)
        except:
            print("Error trying to convert " + filename)
input("\nDone! Press Enter To Exit...")
