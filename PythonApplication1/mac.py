import shutil, os
from os.path import join
print("oof")
theseTypes = [".png", ".jpeg", ".gif", ".mp4", ".mov", ".txt", ".pdf", ".docx", ".doc", ".pages", ".rtf", ".key", ".xls", ".xlsx", ".xlr"]
src = ""
#dead_ends = ["C:\\Dell", "C:\\Intel"]
dst = "\\Volumes\\LMAOBOX\\pc_1"
top = []                                                            #TODO: figure out the top

def detecting_file(thisType):
    if file.endswith(thisType):
        src = join(theDirPath, file)
        print(src)
        try:
            shutil.copy2(src,dst)                                   #TODO: dst should be the correct folder based on its file type 
        except PermissionError:
            print("\n\n\n\n\n\n\n\n\n\n\n\nno permission^\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def not_needed(game):
    if game in theDirNames:
        theDirNames.remove(game)
        
for oneFolder in theseTypes:
    os.makedirs("C:\\Users\\NNguyen\\Desktop\\Newly Created Folder\\{}".format(oneFolder))

for theDirPath, theDirNames, theFileNames in os.walk(top):
    not_needed("Steam")
    not_needed("roblox")
    not_needed("minecraft")    
    for file in theFileNames:
        for oneType in theseTypes:
            detecting_file(oneType)
            #I could make an if command right here to break this for loop when it actually copies so we dont have to go down and finish the list even though it already copied it (save time?)
            # triple for loop has not been tested 8/19/19


b = 0
while b < 3: 
    print("(^_^)")
    b+=1
input("Finished")

