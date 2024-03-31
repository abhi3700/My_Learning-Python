import os

from openai import OpenAI


def main():
    # Create a client
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Blockchain expert."},
            {"role": "user", "content": "What is Subspace Network"},
        ],
    )
    print(chat_completion.choices[0].message.content)


# end def


if __name__ == "__main__":
    main()
