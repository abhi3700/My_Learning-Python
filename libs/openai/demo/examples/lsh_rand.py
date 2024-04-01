"""
Compare multiple queries & if they have same hash, then put them into the same bucket.

Suppose, we decide with 2 hyperplanes with each vector as binary values. And then there are 4 buckets, each of them has 2-dim binary vector.
1. [0, 0]
2. [0, 1]
3. [1, 0]
4. [1, 1]

Then, we can put the queries into the buckets based on the hash of the queries.

Source: https://www.pinecone.io/learn/series/faiss/locality-sensitive-hashing-random-projection/

"""
from typing import Dict, List

import numpy as np

nbits = 4  # number of hyperplanes and binary vals to produce
d = 2  # vector dimensions


def hash_vector(v: List[np.float64], nbits: np.uint16) -> str:
    # create a set of 4 hyperplanes (normal ⟂), with 2 dimensions
    plane_norms = np.random.rand(nbits, d) - 0.5
    print("\nplane_norms")
    print(plane_norms)

    # calculate the dot product for each of these
    v_dot = np.dot(v, plane_norms.T)

    # we know that a positive dot product == +ve side of hyperplane
    # and negative dot product == -ve side of hyperplane
    v_dot = v_dot > 0
    v_dot = v_dot.astype(int)
    v_dot = "".join(str(i) for i in v_dot)

    return v_dot


def put_to_bucket(v: List[str]) -> Dict[str, List[np.uint8]]:
    bucket = {}
    for i, hash_str in enumerate(v):
        if hash_str in bucket:
            bucket[hash_str].append(i)
        else:
            bucket[hash_str] = [i]

    return bucket


# create a set of 4 hyperplanes (normal ⟂), with 2 dimensions
plane_norms = np.random.rand(nbits, d) - 0.5
print("\nplane_norms")
print(plane_norms)
"""
[[-0.27019885  0.09005053]
 [ 0.08076716 -0.32299918]
 [ 0.48026717 -0.39421727]
 [-0.1183272   0.16061436]]
"""

a = np.asarray([1, 2])
b = np.asarray([2, 1])
c = np.asarray([3, 1])
# The lines `d = np.asarray([5, 1])` and `e = np.asarray([2, 3])` are creating NumPy arrays `d` and
# `e` with the specified values.
# d = np.asarray([5, 1])
# e = np.asarray([2, 3])

print("\na, b, c")
print(a)
print(b)
print(c)
# print(d)
# print(e)

# calculate the dot product for each of these
a_dot = np.dot(a, plane_norms.T)
b_dot = np.dot(b, plane_norms.T)
c_dot = np.dot(c, plane_norms.T)
# d_dot = np.dot(d, plane_norms.T)
# e_dot = np.dot(e, plane_norms.T)
print("\na_dot, b_dot, c_dot")
print(a_dot)
print(b_dot)
print(c_dot)
# print(d_dot)
# print(e_dot)


# we know that a positive dot product == +ve side of hyperplane
# and negative dot product == -ve side of hyperplane
a_dot = a_dot > 0
b_dot = b_dot > 0
c_dot = c_dot > 0
print("\na_dot, b_dot, c_dot")
print(a_dot)  # [ True  True  True False]
print(b_dot)  # [ False  True  False False]
print(c_dot)  # [ True  True  False False]

# convert our boolean arrays to int arrays to make bucketing
# easier (although is okay to use boolean for Hamming distance)
print("\na_dot, b_dot, c_dot")
a_dot = a_dot.astype(int)
b_dot = b_dot.astype(int)
c_dot = c_dot.astype(int)
print(a_dot)  # [1 1 1 0]
print(b_dot)  # [0 1 0 0]
print(c_dot)  # [1 1 0 0]

print("\na_dot, b_dot, c_dot")
a_dot = "".join(str(i) for i in a_dot)
b_dot = "".join(str(i) for i in b_dot)
c_dot = "".join(str(i) for i in c_dot)
print(a_dot)  # 1110
print(b_dot)  # 0100
print(c_dot)  # 1100


# Store vectors into respective buckets depending on the hash vector of the embedding vector
bucket = {}
for i, e in enumerate([a_dot, b_dot, c_dot]):
    hash_str = "".join(str(i) for i in e)
    if hash_str in bucket:
        bucket[hash_str].append(i)
    else:
        bucket[hash_str] = [i]

print("\nbucket")
print(bucket)


print("\nM-2:")
print(f"hash vector of a: {hash_vector(a, nbits)}")
print("\nbucket")
bucket = put_to_bucket(
    [hash_vector(a, nbits), hash_vector(b, nbits), hash_vector(c, nbits)]
)
print(bucket)
