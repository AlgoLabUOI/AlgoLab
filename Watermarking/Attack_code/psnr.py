from skimage.metrics import peak_signal_noise_ratio as PSNR
import numpy as np
from PIL import Image
import sys

def calculate_psnr(im1,im2):

	im1 = np.array(Image.open(im1))
	im2 = np.array(Image.open(im2))

	val = PSNR(im1,im2)

	return val



if __name__ == '__main__':
	val = calculate_psnr(sys.argv[1],sys.argv[2])
	print(val)