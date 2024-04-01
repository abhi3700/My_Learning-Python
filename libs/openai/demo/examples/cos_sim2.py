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

from utils import closeness_of_two_queries, display_embedding, get_embedding


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
