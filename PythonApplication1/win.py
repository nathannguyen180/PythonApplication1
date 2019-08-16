import shutil, os
from os.path import join
import string
from ctypes import windll
print("oof")
src = ""
# this is another dead_end "C:\\Users\\NNguyen\\Desktop\\lol"
dead_ends = ["C:\\Dell", "C:\\Intel", "C:\\Log Files", "C:\\Microsoft", "C:\\oracle", "C:\\PerfLogs", "C:\\Windows", "C:\\Program Files (x86)", "C:\\Program Files"]
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives
if __name__ == '__main__':
    print (get_drives())   
usb = input("\nUSB? ")
dst = f"{usb.upper()}:\\LMAOBOX\\pc_1"
#dst = f"{usb.upper()}:\\Users\\NNguyen\\Desktop\\lol\\dst\\lol"
print(dst)
top = []           
a=0        
while a<2:
    buff = input("\nDrive letter? ")
    buff += ":\\"
    top.append(buff.upper())
    print (top)
    buff = ""
    a += 1
def detecting_file(type):
    if file.endswith(type):
        src = join(theDirPath, file)
        print(src)
        try:
            shutil.copy2(src,dst)
        except PermissionError:
            print("\n\n\n\n\n\n\n\n\n\n\n\nno permission^\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
for oneTop in top:
    for theDirPath, theDirNames, theFileNames in os.walk(oneTop):
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
b = 0
while b < 3: 
    print("(^_^)")
    b+=1
input("Finished")
