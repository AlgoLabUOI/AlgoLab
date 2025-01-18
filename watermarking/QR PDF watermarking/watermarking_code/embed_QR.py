import aspose.pdf as pdf  
import qrcode
from PIL import Image 
import numpy as np
import math
import matplotlib.pyplot as plt
import cv2
import random
import sys

def arnold_f(img):
    r, c  = img.shape
    p = np.zeros((r, c), np.uint8)
    a = 1
    b = 1
    for i in range(r):
        for j in range(c):
            x = (i + b * j) % r
            y = (a * i + (a * b + 1) * j) % c
            p[x, y] = img[i, j]
    return p

def create_key(size):
	perm = np.random.permutation(size**2)
	with open("key.txt","w") as f:
		for i in range(len(perm)):
			if(i < len(perm) - 1):
				f.write(str(perm[i])+",")
			else:
				f.write(str(perm[i]))
	f.close()
	return perm

key = create_key(50)

# Load License
license = pdf.License()
license.set_license(sys.argv[1])

inputPDFFile = pdf.Document(sys.argv[2])

for page_n in range(0, len(inputPDFFile.pages)):
    page_number = page_n + 1
    page = inputPDFFile.pages[page_number]

    txtAbsorber = pdf.text.TextFragmentAbsorber()

    page.accept(txtAbsorber)

    textFragmentCollection = txtAbsorber.text_fragments

    extracted_text = txtAbsorber.text

    print(f"The length of the extracted text on page {page_number} is: {len(extracted_text)}")
	
    text_size =  math.floor(math.sqrt(len(extracted_text)))

    # Generate a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(sys.argv[3])
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    qr_img.save(f"qrcode_page_{page_number}.png")

    # Convert the image to grayscale   
    qr_code_gray = qr_img.convert("L")

    # Convert QR code image to a NumPy array
    qr_array = np.array(qr_code_gray)

    # Function to resize the QR code array to match the squared array size
    def resize_qr_code_array(qr_array, text_size):
        r_q_array = cv2.resize(qr_array, dsize=(text_size, text_size), interpolation=cv2.INTER_CUBIC)
        return r_q_array

    print(f"The size of the qr is: {text_size}")

    # Resize the QR code array to match the squared array size
    resized_qr_array = resize_qr_code_array(qr_array, 50)
    
    resized_qr_array_s = Image.fromarray(resized_qr_array)
    resized_qr_array_s.save(f"resized_qr_page_{page_number}.png")    

    resized_qr_array = resized_qr_array.flatten()

    thresholded_qr_array = resized_qr_array.copy()

    for i in range(thresholded_qr_array.shape[0]):
        if thresholded_qr_array[i] >= 128:
            thresholded_qr_array[i] = 255
        else:
            thresholded_qr_array[i] = 0

    arn_img_t = arnold_f(np.reshape(thresholded_qr_array,(50,50)))
    plt.imshow(arn_img_t,cmap = 'gray')
    plt.show()

    count_zero = np.count_nonzero(thresholded_qr_array == 0)
    count_one = np.count_nonzero(thresholded_qr_array == 255)

    print(f"Number of 0 values in the thresholder array: {count_zero}")
    print(f"Number of 255 values in the thresholder array: {count_one}")  

    # Create a dictionary to store numbers (0 and 255) for each letter
    letter_dict = {chr(65 + i): [] for i in range(26)}  # Uppercase letters
    letter_dict.update({chr(97 + i): [] for i in range(26)})  # Lowercase letters

    counter_letter = 0

    arnold_image = arn_img_t.flatten()
    scrambled_qr = np.zeros((50,50)).flatten()
    for i in range(scrambled_qr.shape[0]):
        scrambled_qr[i] = arnold_image[key[i]]

    scrambled_qr = np.reshape(scrambled_qr,(50,50))
    plt.imshow(scrambled_qr,cmap = "gray")
    plt.show()
    scrambled_qr_s = Image.fromarray(scrambled_qr).convert('L')
    scrambled_qr_s.save(f"scrambled_qr_page_{page_number}.png")

    scrambled_arnold_img = scrambled_qr.flatten()

    for txtFragment in textFragmentCollection:
        char = txtFragment.text
        if(counter_letter < len(thresholded_qr_array)):
            if char.isalpha():
                letter_dict[char].append(scrambled_arnold_img[counter_letter])
                counter_letter += 1
                
    print(f"Number of the letters that are extracted to the dictionary: {counter_letter}")
    print(f"Total length of the pdf text: {len(textFragmentCollection)}")
    print(f"The size of the threshold array: {thresholded_qr_array.shape}")

    non_char = []

    newcounter = 0
    char_counter = 0
    count_0 = 0
    count_255 = 0

    for txtFragment in textFragmentCollection:
        char = txtFragment.text
        #print(char)
        if(newcounter < len(thresholded_qr_array)):
            if char.isalpha():
                char_counter += 1
                newcounter += 1
                tmp = letter_dict[char]
                val = tmp.pop(0)
                if(val == 0):
                    random_color = (random.randint(1, 5), 0, 0)
                    txtFragment.text_state.foreground_color = pdf.Color.from_argb(*random_color)
                    count_0 += 1
                else:
                    count_255 += 1
            else:
                non_char.append(char)

    print(f"Number of letters that are readen in the color process: {char_counter}")
    print(f"Number of 0 values after coloring: {count_0}")
    print(f"Number of 255 values after coloring: {count_255}")

    # Save the modified PDF
    inputPDFFile.save(f"colored_text.pdf")