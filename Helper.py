import cv2 as cv
import math
import numpy as np
import Noise
import Color
import os

def Save_Image(data, path, folder_name):
    print("Save_funtion")
    new_path = path + "\\" + folder_name.upper()  # update path
    print(new_path)
    if os.path.exists(new_path):
        sequence = 0
        for img in data:
            cv.imwrite(new_path + "\\" + folder_name + "_%img.PNG" % sequence, img)
            sequence += 1
    else:
        print("Error")

def Convert_white_black(image):
    #convert black to white and white to black
    n_white_pix = np.sum(image == 255)
    n_black_pix = np.sum(image == 0)
    if n_white_pix > n_black_pix:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] == 255:
                    image[i][j] = 0
                elif image[i][j] >= 0:
                    image[i][j] = 255
        return image
    else:
        return image

def Convert_black_white(image):
    #convert black to white and white to black
    n_white_pix = np.sum(image == 255)
    n_black_pix = np.sum(image == 0)
    if n_white_pix < n_black_pix:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] > 150:
                    image[i][j] = 0
                elif image[i][j] == 0:
                    image[i][j] = 255
        return image
    else:
        return image

def rotation(image, angleInDegrees):
    print("Rotation_function")
    h, w = image.shape[:2]
    img_c = (w / 2, h / 2)

    rot = cv.getRotationMatrix2D(img_c, angleInDegrees, 1)

    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_c[0])
    rot[1, 2] += ((b_h / 2) - img_c[1])

    outImg = cv.warpAffine(image, rot, (b_w, b_h), flags=cv.INTER_LINEAR)
    return outImg

def create_simple(image):
    print("Simple_funtion")
    data = []
    sequence = 0
    min = -45; max = 45
    for i in range(min, max, 2):
        img = rotation(image, i)
        img = cv.resize(img, (128, 128))
        img = Convert_black_white(img)
        data.append(img)
        sequence += 1
        shear_val = 0.3
        for shear in range(3):
            img2 = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
            img2 = Shear(img2, i, shear_val)
            shear_val += 0.1
            img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
            img2 = cv.resize(img2, (148, 148))
            img2 = img2[10:138, 10:138]
            img2 = Convert_black_white(img2)
            data.append(img2)
            sequence += 1

    return data

def Shear(original_image, angle, shear):
    print("Shear_funtion")
    # Parameters of the affine transform:
    #angle = 35  # Angle in degrees.
    #shear = 0.3
    translation = 5

    type_border = cv.BORDER_CONSTANT
    color_border = (0, 0, 0)

    #original_image = cv.imread(name)
    rows, cols, ch = original_image.shape

    # First: Necessary space for the rotation
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    cos_part = np.abs(M[0, 0])
    sin_part = np.abs(M[0, 1])
    new_cols = int((rows * sin_part) + (cols * cos_part))
    new_rows = int((rows * cos_part) + (cols * sin_part))

    # Second: Necessary space for the shear
    new_cols += (shear * new_cols)
    new_rows += (shear * new_rows)

    # Calculate the space to add with border
    up_down = int((new_rows - rows) / 2)
    left_right = int((new_cols - cols) / 2)

    final_image = cv.copyMakeBorder(original_image, up_down, up_down, left_right, left_right, type_border, value=color_border)
    rows, cols, ch = final_image.shape

    # Application of the affine transform.
    M_rot = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    translat_center_x = -(shear * cols) / 2
    translat_center_y = -(shear * rows) / 2

    M = M_rot + np.float64([[0, shear, translation + translat_center_x], [shear, 0, translation + translat_center_y]])
    final_image = cv.warpAffine(final_image, M, (cols, rows), borderMode=type_border, borderValue=color_border)

    return final_image

def create_noise(data):
    print("NOise_FUntion")
    noisy_data = []
    take_even_file = 0
    # Now take Salt and Paper Noise on 46 Picture and Total Image Array = 92(Data)
    for item_1 in range(len(data)):
        if take_even_file % 3 == 0:
            img = data[item_1]
            img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
            sp = Noise.sp_noise(img, 0.05)  # Black Salt pepper
            noisy_data.append(sp)
        take_even_file += 1
    for item_2 in range(len(data)):
        if take_even_file % 3 == 1:  # This take only Half Pictures from Folder
            img = data[item_2]
            img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
            SP = Noise.noisy("s&p", img)  # Color S&P
            noisy_data.append(SP)
        take_even_file += 1
    # Now take Salt and Paper Noise on 46 Picture and Total Image Array = 92(Data)
    for item_3 in range(len(data)):
        if take_even_file % 3 == 2:
            img = data[item_3]
            img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
            gauss = Noise.noisy("gauss", img)
            noisy_data.append(gauss)
        take_even_file += 1
    return noisy_data

def create_color(data):
    print("Color_funtion")
    # Now Add Color in Piture
    global color_img
    sequence = 1
    color_data = []
    for img in data:
        if sequence % 3 == 0:
            color_img = Color.color_change(img, "front")
        elif sequence % 3 == 1:
            color_img = Color.color_change(img, "back")
        elif sequence % 3 == 2:
            color_img = Color.color_change(img, "f&b")
        color_data.append(color_img)
        sequence += 1

    return color_data