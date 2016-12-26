import numpy as np
import matplotlib.pyplot as plt

fixed_dim = 50
num_pts = 500
num_eqa = 5
threshold = 1 / np.sqrt(50.)
num_intervals = 100
num_trial = 100

def gen(dim):
	x = []
	for i in range(dim):
		x.append(np.random.normal())
	x /= np.linalg.norm(x)
	return np.array(x)

pt = []
for i in range(num_pts):
	pt.append(gen(fixed_dim))

eq = []
for i in range(num_eqa):
	eq.append(gen(fixed_dim))

cnt = [0] * 5
cnt_all = 0
for i in range(num_pts):
	flag = True
	for j in range(num_eqa):
		if np.abs(np.sum(pt[i] * eq[j])) < 1. * threshold:
			cnt[j] += 1
		else:
			flag = False
	if flag: cnt_all += 1

print cnt
print cnt_all

sat = np.zeros(num_intervals)
for trail in range(num_trial):
	for intv, c in enumerate(np.linspace(0, 7, num_intervals)):
		pt = []
		for i in range(num_pts):
			pt.append(gen(fixed_dim))

		eq = []
		for i in range(num_eqa):
			eq.append(gen(fixed_dim))

		cnt_all = 0
		for i in range(num_pts):
			flag = True
			for j in range(num_eqa):
				if np.abs(np.sum(pt[i] * eq[j])) > c * threshold:
					flag = False
					break
			if flag: cnt_all += 1
		if cnt_all == num_pts:
			sat[intv] += 1 
plt.title('band')
plt.xlabel('round')
plt.ylabel('prob')
plt.plot(np.linspace(0, 7, num_intervals), sat / num_trial, linewidth = 2)
plt.savefig('bands.png', dpi = 240)