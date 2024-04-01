""" 
Break a query (string) into tokens for embedding models of OpenAI.
For GPT-n, the encoding name is different.
"""

from typing import List, Tuple

import tiktoken


def num_tokens_from_string_embedding(
    string: str, encoding_name: str
) -> Tuple[List[int], int]:
    """Returns the number of tokens for a text string for any model"""
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(string)
    num_tokens = len(tokens)
    return tokens, num_tokens


def main():
    query = "What is Subspace Network?"
    # ======= OpenAI embedding models =======
    (tokens, num_tokens) = num_tokens_from_string_embedding(
        query, "cl100k_base"
    )  # for openai embeddings model
    print(
        f'With embedding mode, {query} has tokens: "{tokens}" with {num_tokens} tokens'
    )

    # ======= OpenAI GPT-4 model =======
    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    encoding = tiktoken.encoding_for_model("gpt-4")
    tokens = encoding.encode(query)
    num_tokens = len(tokens)
    print(f'With GPT-4, {query} has tokens: "{tokens}" with {num_tokens} tokens')


if __name__ == "__main__":
    main()
