from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

)
texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]



vector = embedding.embed_documents(texts)

print(vector)
#Here we are not using dotenv to load any api key because HuggingFaceEmbeddings does not require an api key, it runs locally using the specified model. You can change the model_name to any other compatible model from HuggingFace.