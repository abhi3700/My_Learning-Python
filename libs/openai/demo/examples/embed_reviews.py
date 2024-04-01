""" 
Show embeddings for multiple reviews.

TODO: List down the closest ones together and the distant ones away.
"""

import numpy as np

# import pandas as pd
from openai import OpenAI

client = OpenAI()


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


# def main():
#     embedding_model = "text-embedding-3-small"
#     embedding_encoding = "cl100k_base"
#     max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

#     # load & inspect dataset
#     input_datapath = "data/fine_food_reviews_1k.csv"  # to save space, we provide a pre-filtered dataset
#     df = pd.read_csv(input_datapath, index_col=0)
#     df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
#     df = df.dropna()
#     df["combined"] = (
#         "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
#     )
#     print(df.head(2))

#     # subsample to 1k most recent reviews and remove samples that are too long
#     top_n = 1000
#     df = df.sort_values("Time").tail(
#         top_n * 2
#     )  # first cut to first 2k entries, assuming less than half will be filtered out
#     df.drop("Time", axis=1, inplace=True)

#     encoding = tiktoken.get_encoding(embedding_encoding)

#     # omit reviews that are too long to embed
#     df["n_tokens"] = df.combined.apply(lambda x: len(encoding.encode(x)))
#     df = df[df.n_tokens <= max_tokens].tail(top_n)
#     print(len(df))

#     # Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage

#     # This may take a few minutes
#     df["embedding"] = df.combined.apply(
#         lambda x: get_embedding(x, model=embedding_model)
#     )
#     df.to_csv("data/fine_food_reviews_with_embeddings_1k.csv")

#     a = get_embedding("hi", model=embedding_model)
#     print(a)


# # end def


# def main():
#     df = pd.read_csv("data/fine_food_reviews_1k.csv")
#     df["ada_embedding"] = df.ada_embedding.apply(eval).apply(np.array)
#     df["ada_embedding"] = df.combined.apply(
#         lambda x: get_embedding(x, model="text-embedding-3-small")
#     )
#     df.to_csv("data/embedded_1k_reviews.csv", index=False)
# end def


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


# end def


# end def

if __name__ == "__main__":
    print("hello")
    # main()
# end main
