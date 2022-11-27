from encodeinteger import encodeInteger
from decodesip import decodeSip
from embed_key import EmbedPermutation
from extract_sip import ExtractPermutation
from recossip import recsip
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from math import sqrt
import math
from PIL import Image
import itertools as it
import numpy as np
from math import log10, sqrt
from time import process_time
import cv2

import sys
import re

'''
KEY = int(sys.argv[1])
IMAGE = sys.argv[2]
IMAGE_NAME = re.split(r'\.(?!\d)', IMAGE)[0]
COMMAND = sys.argv[3]
COPT = float(sys.argv[4])
global SIP 
global SIZE
'''


def init():
	w = EmbedPermutation()
	ex = ExtractPermutation()

	return w,ex

def mergeCellsToImage(cells,w,h,sip_cells):
	N = len(sip_cells)
	display = np.empty(((w)*N, (h)*N , 3), dtype=np.uint8)

	for i, j in it.product(range(N), range(N)):
		arr = cells[i*N+j]
		
		x,y = i*(w), j*(h)
		display[x : x + (w), y : y + (h)] = arr
			
	
	return display


def openImage(path):
		img = Image.open(path)
		return img


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def ssim_metric(img1,img2):
	image1 = Image.open(img1)
	image2 = Image.open(img2)
	image1 = np.array(image1)
	image2 = np.array(image2)
	value = ssim(image1, image2, data_range=image2.max() - image2.min(),multichannel=True)
	return value


def extract_recsip(im,SIZE,KEY,pr,pb):
	em,ex = init()


	x = 0
	y = 0
	

	img = openImage(im)

	w,h = img.size


	SIP = encodeInteger(KEY)
	SIZE = len(SIP)

	N,M = img.size
	channel_array = np.array(img)


	grid_size_w = math.floor((N / SIZE))
	grid_size_h = math.floor((M / SIZE))

	cells = []

	sip_cells = []

	A_matrix = []
	for i in range(0,len(SIP)):
		row = []
		for j in range(0,SIZE):
			if(j == SIP[i] - 1):
				row.append("*")
				sip_cells.append((i,j))
			else:
				row.append("-")
		A_matrix.append(row)

	i = 0
	for r in range(0,N - grid_size_w + 1, grid_size_w):
		for c in range(0,M - grid_size_h + 1, grid_size_h):

			grid_cell = channel_array[r:r + grid_size_w,c:c + grid_size_h]

			if(i < len(sip_cells) and sip_cells[i][0] == x and sip_cells[i][1] == y):
				

				g_cell = Image.fromarray(grid_cell)
				
				sip1,sip2,sip3 = ex.getSip(g_cell,SIZE,pr,pb)
				
				if(sip1 != SIP):
					n_sip1 = recsip(sip1,SIP,5)
					if(n_sip1 == SIP):
						print("Fixed sip: ",n_sip1)
					else:
						print("Fail!!", n_sip1,sip1)
				elif(sip2 != SIP):
					n_sip2 = recsip(sip2,SIP,5)
					if(n_sip2 == SIP):
						print("Fixed sip: ",n_sip2)
					else:
						print("Fail!!", n_sip2,sip2)
				elif(sip3 != SIP):
					n_sip3 = recsip(sip3,SIP,5)
					if(n_sip3 == SIP):
						print("Fixed sip: ",n_sip3)
					else:
						print("Fail!!", n_sip3,sip3)
				else:
					print("No recostruction needed: \n",sip1,sip2,sip3)
				i += 1
			else:
				cells.append(Image.fromarray(grid_cell))

			y += 1


		x += 1
		y = 0




def recursive_embed(im,sip,size,IMAGE_NAME,COPT,pr,pb):

	em,ex = init()


	x = 0
	y = 0
	

	img = openImage(im)

	w,h = img.size


	SIP = encodeInteger(5)
	SIZE = len(SIP)

	N,M = img.size
	channel_array = np.array(img)


	grid_size_w = math.floor((N / SIZE))
	grid_size_h = math.floor((M / SIZE))

	cells = []

	sip_cells = []

	A_matrix = []
	for i in range(0,len(SIP)):
		row = []
		for j in range(0,SIZE):
			if(j == SIP[i] - 1):
				row.append("*")
				sip_cells.append((i,j))
			else:
				row.append("-")
		A_matrix.append(row)
	

	i = 0
	for r in range(0,N - grid_size_w + 1, grid_size_w):
		for c in range(0,M - grid_size_h + 1, grid_size_h):

			grid_cell = channel_array[r:r + grid_size_w,c:c + grid_size_h]

			if(i < len(sip_cells) and sip_cells[i][0] == x and sip_cells[i][1] == y):
				

				g_cell = Image.fromarray(grid_cell)
				
				w_im = em.getWatermarkedImage(g_cell,sip,size,IMAGE_NAME,COPT,pr,pb)
				cells.append(w_im)
				i += 1
			else:
				cells.append(Image.fromarray(grid_cell))

			y += 1


		x += 1
		y = 0

	img = mergeCellsToImage(cells,grid_size_w,grid_size_h,sip_cells)
	img = cv2.resize(np.array(img),(w,h),interpolation = cv2.INTER_AREA)
	img = Image.fromarray(img)
	img.save("watermarked_" + IMAGE_NAME + "_1" + ".jpg",quality = 100)

	return img
				

