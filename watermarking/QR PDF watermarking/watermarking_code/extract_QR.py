import aspose.pdf as pdf  
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
#import embed_qr
import sys

def dearnold(img):
    r, c = img.shape
    p = np.zeros((r, c), np.uint8)
    a = 1
    b = 1
    for i in range(r):
        for j in range(c):
            x = ((a * b + 1) * i - b * j) % r
            y = (-a * i + j) % c
            p[x, y] = img[i, j]
    return p

def get_key():
	with open("key.txt","r") as f:
		key = f.readlines()
	key = key[0].split(',')
	return key

the_key = get_key()

license = pdf.License()
license.set_license(sys.argv[1])

colored_pdf = pdf.Document("colored_text.pdf")

for page_n in range(0, len(colored_pdf.pages)):
    page_number = page_n + 1
    page = colored_pdf.pages[page_number]
	
    txtAbsorber = pdf.text.TextFragmentAbsorber()

    page.accept(txtAbsorber)

    textFragmentCollection = txtAbsorber.text_fragments

    bin_array = []

    bin_array = np.zeros((50,50)).flatten()
    s_array = np.zeros((50,50)).flatten()
    char_counter = 0

    # Iterate through the extracted text and apply color changes
    for txtFragment in textFragmentCollection:
        char = txtFragment.text
        if(char_counter < 2500):
            color = txtFragment.text_state.foreground_color
            #print(f"Character: {char}, Color: {color}")
            if char.isalpha():
                if(color != pdf.Color.from_argb(0, 0, 0)):
                    bin_array[int(the_key[char_counter])] = 0
                    s_array[char_counter] = 0 # attacker can only do this if he doesnt know the key
                else:
                    bin_array[int(the_key[char_counter])] = 255
                    s_array[char_counter] = 255
                char_counter += 1  


    s_array = np.array(s_array).reshape((50,50))
    plt.imshow(s_array,cmap = 'gray')
    (Image.fromarray(s_array).convert('L')).save(f"without_key_page_{page_number}.png")

    bin_array = np.array(bin_array).reshape((50,50))
    plt.imshow(bin_array,cmap = 'gray')
    (Image.fromarray(bin_array).convert('L')).save(f"with_key_page_{page_number}.png")

    dearn_img = dearnold(bin_array)
    plt.imshow(dearn_img,cmap = 'gray')
    (Image.fromarray(dearn_img).convert('L')).save(f"extracted_qr_page_{page_number}.png")