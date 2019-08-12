import shutil, os
from os.path import join
print("oof")
src = ""
dst = "C:\\Users\\NNguyen\\Desktop\\lol\\GREAT"
#top = ["C:\\Users\\", "C:\\Program Files\\", "C:\\Program Files (x86)\\"]
top = "C:\\"
sub = []
#top = ["C:\\Users\\NNguyen\\Desktop\\test\\test_1", "C:\\Users\\NNguyen\\Desktop\\test\\test_2", "C:\\Users\\NNguyen\\Desktop\\test\\test_3"]
#useless = ['Windows', 'PerfLogs', 'oracle', 'Microsoft', 'Log Files', 'Intel', 'Dell']
for realTop in top:
    for theDirPath, theDirNames, theFileNames in os.walk(realTop):
        if "1AZN$WAG.txt" in theFileNames:
            print("double oof")
            break
        if '\\Dell' in theDirPath:
            theDirNames.remove('\\Windows', '\\PerfLogs', '\\oracle', '\\Microsoft', '\\Log Files', '\\Intel', '\\Dell')  # don't visit these directories
        print(theDirPath)
    #    if 'dotnet' in dirs:
    #        dirs.remove('dotnet') 
    #    if 'Android' in dirs:
    #        dirs.remove('Android')
       # for file in theFileNames:
           # if file.endswith(".txt"):
               # src = join(theDirPath, file)
               # print(src)
               # shutil.copy2(src,dst)
def findit(root, exclude_dirs=[]):
    exclude_dirs = (os.path.normpath(i) for i in exclude_dirs)
    exclude_dirs = (os.path.normcase(i) for i in exclude_dirs)
    exclude_dirs = set(exclude_dirs)
    for current, dirs, files in os.walk(root):
        if os.path.normpath(os.path.normcase(current)) in exclude_dirs:
            # exclude this dir and subdirectories
            dirs[:] = []
            continue
        for f in files:
            if not exclude_files.match(os.path.normcase(f)):
                yield os.path.join(current, f)

a=0
while a < 3: 
    print("(^_^)")
    a+=1

        #".txt", ".pdf", ".png", ".jpeg", ".xlsx"):
#https://stackabuse.com/creating-and-deleting-directories-with-python/
#https://www.pyinstaller.org/features.html
#https://www.google.com/search?q=pyinstaller&ie=&oe=
#https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory