""" 
# Show embeddings example using OpenAI's embedding models (small, large)

## Key points

- The embeddings are deterministic. If you run the same query twice, you will get the same embedding.

## Semantic Hashing

How to determine closeness (proximity) of the semantics of 2 queries?
It can be measured by a dot product of their corresponding embeddings (vectors). But, which query to use as the base?

TODO: Refine this docs below:
So, another approach could be calculating hashing (with some dimension) for each query. Then the hash comparison can be done to find the closest query, rather than some dot product. 
Not sure if this is the right approach. Because may be mathematically, the semantic hash of queries comes out to be a little different by a few bits relatively.

For this, we have to first determine the dimension of the embeddings.
"""

import numpy as np
from openai import OpenAI

client = OpenAI()


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def display_embedding(query, embedding):
    """
    Purpose: Print just the first 5 and last 5 elements of the embedding
    """
    print(f"\n{query}")
    print(embedding[:5])  # Show first 5 elements
    print(embedding[-5:])  # Show last 5 elements


def closeness_of_two_queries(q1, q2):
    """
    Purpose: Difference b/w two queries. If it's close to 1, then they have more closer semantic meaning.
    Maths: dot product of two embeddings is the cosine similarity. In maths & physics, dot product is used
    to capture the notion of how much one vector goes in the direction of another.

    The embeddings vectors were deterministic 🤔.

    Tested with 2 exact same queries, the dot product was 0.99999999..
    """
    e1 = get_embedding(q1)
    e2 = get_embedding(q2)
    return np.dot(e1, e2)


def main():
    q1 = "How to make a cake?"
    q2 = "How to bake a cake?"
    q3 = "How to cook a cake?"

    e1 = get_embedding(q1)
    display_embedding(q1, e1)

    e2 = get_embedding(q2)
    display_embedding(q2, e2)

    e3 = get_embedding(q3)
    display_embedding(q3, e3)

    print(f"\n{q1} vs {q2} = {closeness_of_two_queries(q1, q2)}")
    print(f"\n{q2} vs {q3} = {closeness_of_two_queries(q2, q3)}")
    print(f"\n{q1} vs {q3} = {closeness_of_two_queries(q1, q3)}")

    # ======= Test with similar queries =========

    q4 = "He wants to build a house made of rocks."
    q5 = "He wants to build a house made of stones."
    print(f"\n{q4} vs {q5} = {closeness_of_two_queries(q4, q5)}")


if __name__ == "__main__":
    main()
