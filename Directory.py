import os

def Dir(dirName,Folders):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    path = os.path.join(desktop, dirName)
    try:
        # Create target Directory
        os.mkdir(path)
        # print("Directory ", dirName, " Created ")
    except FileExistsError:
        pass
        #print("Directory ", dirName, " already exists")

    if os.path.exists(path):
        for folder in Folders:
            folder_name = folder.split('\\')
            folder_name = folder_name[-1].split('.')
            folder_path = os.path.join(path, (folder_name[0].upper()))
            try:
                # Create target Directory
                os.mkdir(folder_path)
                # print("Directory ", folder_name[0].upper(), " Created ")
            except FileExistsError:
                pass
                #print("Directory ", folder_name[0], " already exists")
    else:
        print("Error")