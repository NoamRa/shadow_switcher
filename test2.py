import numpy as np


def threshold_limit(orig, threshold, limit):
	# threshold_limit recives orig (int), threshold (int), and limit (int).
	# adds oring and threshold. if the result is above limit the result is clipped.
	# subtracts oring from threshold. if the result is below 0, the result is clipped.
	# returns max_out (int) and min_out (int)
	if (orig + threshold) > limit:
		max_out = limit
	else:
		max_out = orig + threshold

	if (orig - threshold) < 0:
		min_out = 0
	else:
		min_out = orig - threshold

	return max_out, min_out


#orig = np.uint8([[[50, 155, 255]]])
orig = 100

#print "input is 240"
print threshold_limit(orig, 80, 179)
print 
print threshold_limit(orig, 50, 179)