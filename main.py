import character
import Helper
import Directory
import os
import time
from tqdm import tqdm

def main():
    names, images = character.charList()

    # if len(sys.argv) != 2:
    #     print('usage: main.py <dir_name>', file=sys.stderr)
    #     sys.exit(1)

    # dirName = sys.argv[1]
    dirName = "Data_set"
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = os.path.join(desktop, dirName)

    Directory.Dir(dirName, names)
    for img in range(len(images)):
        Name = names[img].split('\\')
        Name = Name[-1].split('.')
        print(Name[0].upper(),"Progressing....")
        Simple_data = Helper.create_simple(Helper.Convert_white_black(images[img]))

        Noise_data = Helper.create_noise(Simple_data)

        Color_data = Helper.create_color(Noise_data)

        for i in tqdm(range(len(Color_data))):
            time.sleep(0.01)

        folder_name = names[img].split('\\')
        folder_name = folder_name[-1].split('.')

        Helper.Save_Image(Color_data, path, folder_name[0].upper())

if __name__ == '__main__':
    main()
