import character
import Helper
import Directory
import os

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
        Simple_data = Helper.create_simple(Helper.Convert_white_black(images[img]))
        #print(len(Simple_data))

        Noise_data = Helper.create_noise(Simple_data)
        #print(len(Noise_data))

        Color_data = Helper.create_color(Noise_data)
        #print(len(Color_data))

        folder_name = names[img].split('\\')
        folder_name = folder_name[-1].split('.')
        folder_path = os.path.join(path, (folder_name[0].upper()))

        Helper.Save_Image(Color_data, path, folder_name[0].upper())


if __name__ == '__main__':
    main()
