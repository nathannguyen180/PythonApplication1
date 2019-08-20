import shutil, os
from os.path import join
print("oof")
theseTypes = [".png", ".jpeg", ".gif", ".mp4", ".mov", ".txt", ".pdf", ".docx", ".doc", ".pages", ".rtf", ".key", ".xls", ".xlsx", ".xlr"]
src = ""
#dead_ends = ["C:\\Dell", "C:\\Intel"]
#dst = "\\Volumes\\LMAOBOX\\pc_1"
dst = "C:\\Users\\NNguyen\\Desktop\\Newly Created Folder"
top = "C:\\"                                                            #TODO: figure out the top in mac OS

for oneFolder in theseTypes:
    os.makedirs("{}\\{}".format(dst, oneFolder))

def detecting_file(thisType):
    if file.endswith(thisType):
        src = join(theDirPath, file)
        print(src)
        try:
            shutil.copy2(src, "{}\\{}".format(dst, thisType))                                  
        except PermissionError:
            print("\n\n\n\n\n\n\n\n\n\n\n\nno permission^\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def not_needed(game):
    if game in theDirNames:
        theDirNames.remove(game)
       
for theDirPath, theDirNames, theFileNames in os.walk(top):
    not_needed("Steam")
    not_needed("roblox")
    not_needed("minecraft")
    for file in theFileNames:
        for oneType in theseTypes:
            detecting_file(oneType)
            #I could make an if command right here to break this for loop when it actually copies so we dont have to go down and finish the list even though it already copied it (save time?)
            


b = 0
while b < 3: 
    print("(^_^)")
    b+=1
input("Finished")

