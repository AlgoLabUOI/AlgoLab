import os , sys
from collections import Counter


def passes(s,sip,key,mod):
	if(mod == "left"):
		pairs = []

		for i in range(len(s)):
			pairs.append((i+1,s[i]))

		recostructed_sip = []

		k = int(len(pairs) / 2)
		for i in range(0,k):
			x = pairs[i][0]
			y = pairs[i][1]

			rev = (y,x)

			if(rev in pairs):
				pass
			else:
				pairs[y - 1] = (y,x)
		

		for i in range(len(pairs)):
			recostructed_sip.append(pairs[i][1])

		return recostructed_sip

	if(mod == "right"):
		pairs = []

		for i in range(len(s)):
			pairs.append((i+1,s[i]))

		recostructed_sip = []

		k = int(len(pairs) / 2)
		for i in range(len(pairs)-1,k,-1):
			x = pairs[i][0]
			y = pairs[i][1]

			rev = (y,x)

			if(rev in pairs):
				print(pairs[i])
				pass
			else:
				print(pairs[i])
				pairs[y - 1] = (y,x)
		

		for i in range(len(pairs)):
			recostructed_sip.append(pairs[i][1])

		return recostructed_sip

	if(mod == "middle"):
		pairs = []
		recostructed_sip = []

		for i in range(len(s)):
			pairs.append((i+1,s[i]))

		for i in range(len(pairs)):
			x = pairs[i][0]
			y = pairs[i][1]

			rev = (y,x)

			if(rev in pairs):
				pass
			else:
				pairs[x - 1] = (x,x)

		for i in range(len(pairs)):
			recostructed_sip.append(pairs[i][1])

		return recostructed_sip

	if(mod == "start"):
		B = list(bin(key)[2:])
		k = len(B)

		recostructed_sip = []

		for i in range(len(s)):
			recostructed_sip.append(s[i])

		
		recostructed_sip[0] = k + 1
		recostructed_sip[k] = 1


		return recostructed_sip

def recsip(extracted_sip,sip,key,pass_sequence):
	recostructed_sip = 0
	if(extracted_sip != sip):
		recostructed_sip = passes(extracted_sip,sip,key,'start')
		if(recostructed_sip != sip):
			recostructed_sip = passes(recostructed_sip,sip,key,'left')

			if(recostructed_sip != sip):
				recostructed_sip = passes(recostructed_sip,sip,key,'middle')
	else:
		return extracted_sip

		

	
	return recostructed_sip


if __name__ == '__main__':
	a = recsip( [4, 6, 7, 1, 7, 2, 3],[4,6,7,1,5,2,3],5,["start","left","middle"])
	print(a)