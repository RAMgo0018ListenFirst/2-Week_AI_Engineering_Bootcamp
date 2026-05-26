from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions=64
)

texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]

vector = embeddings.embed_documents(texts)

print(vector)
#Here we are using dotenv to load the OPENAI_API_KEY from the .env file, you can set it in your .env file or export it in your terminal. You can also change the model to any other compatible model from OpenAI.