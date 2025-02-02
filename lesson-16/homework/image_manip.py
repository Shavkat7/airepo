from PIL import Image
import numpy as np

with Image.open('lesson-16/birds.jpg') as img:
      arr = np.array(img)



# REVERSING IMAGE VERTICALLY AND HORIZONTALLY
# vertical_reversed = Image.fromarray(arr[::-1, :, :])
# vertical_reversed.save("lesson-16/vertical_reversed.jpg")
# horizontal_reversed = Image.fromarray(arr[:, ::-1, :])
# horizontal_reversed.save("lesson-16/horizontal_reversed.jpg")


# ADDING RANDOM NOISE
# import random


# noise_arr_img = arr

# for row in noise_arr_img:
#       for pix in row:
#             for rgb in range(len(pix)):
#                   if 30 <= pix[rgb] <= 230:
#                     new_value = int(pix[rgb]) + random.randint(-70, 70)
#                     pix[rgb] = np.clip(new_value, 0, 255).astype(np.uint8)


# noisy_img = Image.fromarray(noise_arr_img)
# noisy_img.save("lesson-16/noisy_img.jpg")


# INCREASE RED-COLOR INTENSITY

# intense_red = arr
# intense_red[:, :, 0] = np.clip(intense_red[:, :, 0] + 40, 0, 255)

# intense_red_img = Image.fromarray(intense_red)
# intense_red_img.save("lesson-16/intense-red.jpg")



# APPLY A MASK (BLACK BOX 100X100 IN THE CENTER OF THE IMAGE)
# 360 - 49 = 311 ; 361 + 49 = 410

# masked_arr = arr

# masked_arr[311:411, 311:411, :] = 0

# masked_arr_img = Image.fromarray(masked_arr)
# masked_arr_img.save("lesson-16/maked_img.jpg")

# BONUS FUNCTIONS

# def flip_image(arr1):
#     vertical_reversed = Image.fromarray(arr1[::-1, :, :])
#     vertical_reversed.save("lesson-16/vertical_reversed.jpg")
#     horizontal_reversed = Image.fromarray(arr1[:, ::-1, :])
#     horizontal_reversed.save("lesson-16/horizontal_reversed.jpg")


# def add_noise(arr1):
#     import random

#     noise_arr_img = arr1

#     for row in noise_arr_img:
#         for pix in row:
#                 for rgb in range(len(pix)):
#                     if 30 <= pix[rgb] <= 230:
#                         new_value = int(pix[rgb]) + random.randint(-70, 70)
#                         pix[rgb] = np.clip(new_value, 0, 255).astype(np.uint8)


#     noisy_img = Image.fromarray(noise_arr_img)
#     noisy_img.save("lesson-16/noisy_img.jpg")


# def brighten_channels(arr1, i):
#     intense_red = arr1
#     intense_red[:, :, i] = np.clip(intense_red[:, :, i] + 40, 0, 255)

#     intense_red_img = Image.fromarray(intense_red)
#     intense_red_img.save("lesson-16/intense-red.jpg")


# def apply_mask(arr1):
#     masked_arr = arr1

#     masked_arr[311:411, 311:411, :] = 0

#     masked_arr_img = Image.fromarray(masked_arr)
#     masked_arr_img.save("lesson-16/maked_img.jpg")