def getfiles(directory):# Get the list of all files in directory tree at given path
    import os
    listoffiles = list()
    for (dirpath, dirnames, filenames) in os.walk(directory):
        listoffiles += [os.path.join(dirpath, file) for file in filenames]
    return listoffiles

#check the function
directory = r'c:\Группа Лобачевского Dropbox'
print(getfiles(directory))