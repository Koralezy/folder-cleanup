import os

print("Type your keywords/phrases separated by new lines and press ENTER twice when done.")
keywds = []
while True:
    e = input()
    if e == "":
        break
    else:
        keywds.append(e)


startdir = input("Type the origin folder path here: ")
try:
    startdir = startdir.replace('"', '')
except:
    pass

enddir = input("Type the destination folder path here: ")
try:
    enddir = enddir.replace('"', '')
except:
    pass

while True:
    if enddir == startdir:
        enddir = input("The origin cannot be the same as the destination. Please type a path to a DIFFERENT folder: ")
    else:
        break


errorlist = {}
for filename in os.listdir(startdir):
    file = os.path.join(startdir, filename)

    if os.path.isfile(file):
        for word in keywds:
            if word.lower() in file.lower():
                newfile = os.path.join(enddir, filename)
                try:
                    os.rename(file, newfile)
                    print("Moved", filename, " Keyword:", word)
                except Exception as error:
                    fullerr = f"{type(error).__name__} - {error}"
                    print("An error occurred: ",fullerr)
                    errorlist[filename] = fullerr


print("Done!")
if len(errorlist) > 0:
    a = input(f"We found {len(errorlist)} error(s). Press ENTER to see them.")
    if a != "" or a == "":
        for x, y in errorlist.items():
            print(f"File: {x} - Error: {y}")