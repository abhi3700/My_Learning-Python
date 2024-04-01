""" 
Cosine similarity using sklearn lib.

## Key points

- The embeddings are deterministic. If you run the same query twice, you will get the same embedding.
- The cosine similarity is a measure of similarity between two non-zero vectors of an inner product 
space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than
1 for any other angle.
- For exact same text, it's going to be 0.999999, bcoz the embedding vectors are exactly same.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import display_embedding, get_embedding


def cos_sim(vector1, vector2):
    vector1_2d = np.array(vector1).reshape(1, -1)
    vector2_2d = np.array(vector2).reshape(1, -1)
    return cosine_similarity(vector1_2d, vector2_2d)


# Example usage:

q1 = "How to make a cake?"
q2 = "How to bake a cake?"
q3 = "How to cook a cake?"

e1 = get_embedding(q1)
display_embedding(q1, e1)

e2 = get_embedding(q2)
display_embedding(q2, e2)


similarity = cos_sim(e1, e2)
print(f"\n{q1} vs {q2} = {similarity[0][0]}")
