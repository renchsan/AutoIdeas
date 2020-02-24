import os
import zipfile


# with zipfile.ZipFile('archive.zip') as z:
with zipfile.ZipFile('DAVID-Spade-Grip.zip') as z:
    for filename in z.namelist():
        print(filename)
        if filename.endswith(".stl" or ".STL"):
            print(filename)
            
