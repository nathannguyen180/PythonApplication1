import shutil, os
from os.path import join#, getsize

#C:\\Users\\NNguyen\\Desktop\\old Csharp.txt
src = ""
dst = "C:\\lol\\biglol"
top = "C:\\Users\\NNguyen\\Desktop"



#os.path.join(top, "Basic Calculator.txt")

print()



for theDirPath, theDirNames, theFileNames in os.walk(top):
    #print(theDirPath, "consumes", end=" ")
    #print(sum(getsize(join(theDirPath, name)) for name in theFileNames), end=" ")
    #print("bytes in", len(theFileNames), "non-directory files\n")
    
    for file in theFileNames:
        if file.endswith(".txt"):
            src = join(theDirPath, file)
            print(src)
            shutil.copy2(src,dst)

            

#    if 'Microsoft' in dirs:
#        dirs.remove('Microsoft')  # don't visit these directories
#    if 'dotnet' in dirs:
#        dirs.remove('dotnet') 
#    if 'Android' in dirs:
#        dirs.remove('Android') 