import cv2
import numpy as np

def preserve(channel, ratio):
	U, s, V = np.linalg.svd(channel)
	sz = int(min(U.shape[0], V.shape[0]) * ratio)
	S = np.zeros((U.shape[0], V.shape[0]))
	S[:sz, :sz] = np.diag(s[: sz])
	return np.dot(U, np.dot(S, V))

def gen(channels, ratio):
	ret = []
	for channel in channels:
		ret.append(preserve(channel, ratio))
	return np.stack(ret, axis = 2)

img = cv2.imread('dw.jpg')
for ratio in [.05, .1, .25, .50]:
	gen_img = gen([img[:, :, 0], img[:, :, 1], img[:, :, 2]], ratio)
	cv2.imwrite('dw' + str(int(100 * ratio)) + '.png', gen_img)
	print np.linalg.norm(gen_img) / np.linalg.norm(img)



