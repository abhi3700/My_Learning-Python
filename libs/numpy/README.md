# Numpy
## Features
* Faster than lists as it is fixed type, requires less bytes of memory (contiguous).
* Mathematics Replacement for Matlab
* Does plotting
* backend for Plotting, Connect 4, Digital Photography
* Machine Learning (Tensorflow built similar to numpy)


## Coding
* Import package
```py
import numpy as np
```
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
* Vector
```py
a = np.array([1, 2, 3, 4])
```
* Matrix
```py
matrix_obj = np.matrix([[1, 2],
												[1, 2],
												[1, 2]])
```
	- matrix func is not used because:
		+ arrays are the de facto standard data structure of NumPy
		+ vast majority of NumPy operations return arrays, not matrix objects

## Concepts
* Normal Distribution (like Gaussian Distribution) has 3 main params:
	- __loc__ i.e. mean, where the peak of the bell exists or the centre of the distribution
	- __scale__ i.e. Standard Deviation, how much flat the curve is, or spread or “width” of the distribution. Must be non-negative.
	- __size__ i.e. shape of the returned array
	- Resources:
		+ [numpy.random.normal by Numpy docs](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
		+ [Oreilly Chapter 1. Vectors, Matrices, and Arrays](https://www.oreilly.com/library/view/machine-learning-with/9781491989371/ch01.html)