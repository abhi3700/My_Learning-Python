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


* Sparse Matrix
	- SciPy provides tools for creating sparse matrices using multiple data structures, as well as tools for converting a dense matrix to a sparse matrix.
	- Many linear algebra NumPy and SciPy functions that operate on NumPy arrays can transparently operate on SciPy sparse arrays. Further, machine learning libraries that use NumPy data structures can also operate transparently on SciPy sparse arrays, such as scikit-learn for general machine learning and Keras for deep learning.
	- NumPy does not provide a function to calculate the sparsity of a matrix.

## Concepts
* Sparse Matrix
	- Def:
	- Mathematics
```
sparsity = count zero elements / total elements

     1, 0, 0, 1, 0, 0
A = (0, 0, 2, 0, 0, 1)
     0, 0, 0, 2, 0, 0

The example has 13 zero values of the 18 elements in the matrix, giving this matrix a sparsity score of 0.722 or about 72%.
```
	- Sparse matrices come up in some specific types of data, most notably observations that record the occurrence or count of an activity.
	- Data examples:
		+ Whether or not a user has watched a movie in a movie catalog.
		+ Whether or not a user has purchased a product in a product catalog.
		+ Count of the number of listens of a song in a song catalog.
	- Data preparation - Encoding schemes:
		+ One-hot encoding, used to represent categorical data as sparse binary vectors.
		+ Count encoding, used to represent the frequency of words in a vocabulary for a document
		+ TF-IDF encoding, used to represent normalized word frequency scores in a vocabulary.
	- Some areas of study within machine learning must develop specialized methods to address sparsity directly as the input data is almost always sparse.
		+ Natural language processing for working with documents of text.
		+ Recommender systems for working with product usage within a catalog.
		+ Computer vision when working with images that contain lots of black pixels.
	- Problems: space & time complexity
		+ In practice, most large matrices are sparse — almost all entries are zeros.
		+ This is clearly a waste of memory resources as those zero values do not contain any information.
		+ This is a problem of increased time complexity of matrix operations that increases with the size of the matrix.
	- The Compressed Sparse Row, also called CSR for short, is often used to represent sparse matrices in machine learning given the efficient access and matrix multiplication that it supports.

* Normal Distribution (like Gaussian Distribution) has 3 main params:
	- __loc__ i.e. mean, where the peak of the bell exists or the centre of the distribution
	- __scale__ i.e. Standard Deviation, how much flat the curve is, or spread or “width” of the distribution. Must be non-negative.
	- __size__ i.e. shape of the returned array
	- Resources:
		+ [numpy.random.normal by Numpy docs](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
		+ [Oreilly Chapter 1. Vectors, Matrices, and Arrays](https://www.oreilly.com/library/view/machine-learning-with/9781491989371/ch01.html)