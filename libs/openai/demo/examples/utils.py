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
