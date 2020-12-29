# Numpy
## Features
* Faster than lists as it is fixed type, requires less bytes of memory (contiguous).
* Mathematics Replacement for Matlab
* Does plotting
* backend for Plotting, Connect 4, Digital Photography
* Machine Learning (Tensorflow built similar to numpy)


## Coding
* multiplication
```py
# in case of list
a = [1, 3, 4]
b = [4, 6, 8]
a*b = ERROR

# in case of numpy
a = np.array(1, 3, 4)
b = np.array(4, 6, 8)
a*b = np.array([4. 18. 32])
```

## Concepts
* Normal Distribution (like Gaussian Distribution) has 3 main params:
	- __loc__ i.e. mean, where the peak of the bell exists
	- __scale__ i.e. Standard Deviation, how much flat the curve is
	- __size__ i.e. shape of the returned array