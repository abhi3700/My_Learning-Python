""" 
Break a query (string) into tokens
"""

import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def main():
    query = "What is Subspace Network?"
    num_tokens = num_tokens_from_string(query, "cl100k_base")
    print(f'No. of tokens in "{query}" is {num_tokens}')


if __name__ == "__main__":
    main()
