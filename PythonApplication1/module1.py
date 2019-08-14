import shutil, os
from os.path import join
print("oof")
src = ""
#dst = "E:\\LMAOBOX\\pc_1"
dead_ends = ["C:\\Dell", "C:\\Intel", "C:\\Log Files", "C:\\Microsoft", "C:\\oracle", "C:\\PerfLogs", "C:\\Windows", "C:\\Program Files (x86)", "C:\\Program Files", "C:\\Users\\NNguyen\\Desktop\\lol"]
dst = "C:\\Users\\NNguyen\\Desktop\\lol\\dst"
top = ["C:\\Users", "D:\\"]
answer = input("Full? ")
if answer == 'y':
    top = ["C:\\", "D:\\"]
print (top)

def detecting_file(type):
    if file.endswith(type):
        src = join(theDirPath, file)
        print(src)
        try:
            shutil.copy2(src,dst)
        except PermissionError:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nno permission\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
for oneTop in top:
    for theDirPath, theDirNames, theFileNames in os.walk(oneTop):
        if "1AZN$WAG" in theDirNames:
            print("double oof")
            break
        if theDirPath in dead_ends:
            # exclude this dir and subdirectories 
            theDirNames[:] = []
            continue
        else:
            for file in theFileNames:
                detecting_file(".txt")
                detecting_file(".png")
                detecting_file(".pdf")
                detecting_file(".jpeg")
                detecting_file(".docx")
                detecting_file(".xlsx")
                detecting_file(".xls")
a = 0
while a < 3: 
    print("(^_^)")
    a+=1
input("Finished")
