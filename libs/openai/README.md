# OpenAI package

## Quickstart

Refer this [quickstart](https://platform.openai.com/docs/quickstart?context=python) for python.

## Embeddings

Embeddings are like numeric values for semantic meaning of search query.

Imagine, a person searches for "how to make a cake". Now, to store this query in a database to quickly verify it has been generated via LLM, we would initially try to hash the string and store it. But, this is not efficient as the same person might search for "how to bake a cake" and we would have to store this as well. This is not efficient as how many variations of the same query can we store?

So, we need a way to store the semantic meaning of the query. This is where embeddings come into play. Also, called "Semantic embeddings or hashing".

Refer this [guide](https://platform.openai.com/docs/guides/embeddings).

I tried this with `curl`. [Output](./embeddings.json).

```sh
curl https://api.openai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "input": "What is subspace network?",
    "model": "text-embedding-3-small"
  }' > embeddings.json
```

## References

- [OpenAI cookbook](https://cookbook.openai.com/)
- [OpenAI Developer platform](https://platform.openai.com/docs/overview)
- [OpenAI Developer API](https://platform.openai.com/docs/api-reference)
- [Developer API for Embeddings](https://platform.openai.com/docs/api-reference/embeddings)
