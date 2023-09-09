import openai
import pandas as pd

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

def create_embeddings(input: str):
    return openai.Embedding.create(input=input, model="text-embedding-ada-002")["data"][0]["embedding"]

# search function
def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    query_embedding = create_embeddings(query)
    strings_and_relatednesses = [
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

def relatedness_fn(x, y):
    return 1 - spatial.distance.cosine(x, y)


def answer_question_for_value(app_name: str, value: str, eula: str):
    query = f"""Use the below end user license agreement for {app_name} to determine how it affects someone who values {value}. Return the response as bullet points and nothing else.

\"\"\"
{eula}
\"\"\""""

    response = openai.ChatCompletion.create(
        messages=[
            {'role': 'system', 'content': f'You are a lawyer reviewing the end user license agreement for {app_name} on behalf of a user who values {value}.'},
            {'role': 'user', 'content': query},
        ],
        model=GPT_MODEL,
        temperature=0,
    )

    return response['choices'][0]['message']['content']
