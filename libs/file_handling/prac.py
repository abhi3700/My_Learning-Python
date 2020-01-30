import shutil
import  os
import getpass
# src = "C:\\Users\\abhijit\\Desktop\\1_2.gif"
# des = "."
username = getpass.getuser()
filename = "REPL1A_Nit_ER-Plot.html"
print(getpass.getuser())
src = "C:/Users/{username}/OneDrive/Documents/{filename}"
src = src.format(username = username, filename= filename)

folder_path = "C:/Users/{username}/OneDrive/Documents/".format(username = username)
for f in os.listdir(folder_path):
    if f.endswith(".html"):
        os.remove(folder_path+f)

des = "REPL1A_CP-Plot.html"
# shutil.copy(src, des)
print(os.listdir("."))
print(os.path.abspath("."))