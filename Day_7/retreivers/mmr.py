# Import the Document class
# A Document is used to store text data inside LangChain
from langchain_core.documents import Document

# Import Chroma vector database
# Chroma stores embeddings (numerical vectors of text)
from langchain_community.vectorstores import Chroma

# Import HuggingFace embeddings model
# Embeddings convert text into numerical vectors
from langchain_community.embeddings import HuggingFaceEmbeddings


# ------------------------------------------------------
# STEP 1: Create documents
# ------------------------------------------------------

# We are creating a list of documents.
# Each document contains some text related to machine learning.

docs = [
    
    # Document about gradient descent
    Document(
        page_content="Gradient descent is an optimization algorithm used in machine learning."
    ),

    # Another document related to gradient descent
    Document(
        page_content="Gradient descent minimizes the loss function."
    ),

    # Similar sentence with slightly different wording
    Document(
        page_content="Gradient descent is an optimization that minimizes the loss function."
    ),

    # Document about neural networks
    Document(
        page_content="Neural networks use gradient descent for training."
    ),

    # Completely different topic
    Document(
        page_content="Support Vector Machines are supervised learning algorithms."
    )
]


# ------------------------------------------------------
# STEP 2: Create embeddings model
# ------------------------------------------------------

# HuggingFaceEmbeddings converts text into vectors.
# Similar texts will have similar vectors.

embeddings = HuggingFaceEmbeddings()


# ------------------------------------------------------
# STEP 3: Store documents in Chroma vector database
# ------------------------------------------------------

# Chroma.from_documents():
# 1. Takes documents
# 2. Converts them into embeddings
# 3. Stores them inside vector database

vectorstore = Chroma.from_documents(
    docs,          # List of documents
    embeddings     # Embedding model
)


# ------------------------------------------------------
# STEP 4: Create Similarity Retriever
# ------------------------------------------------------

# as_retriever() converts vectorstore into a retriever.

# search_type="similarity"
# -> Retrieves documents most similar to the query.

# search_kwargs={"k":3}
# -> Return top 3 most relevant documents.

similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# Print heading
print("\n===== Similarity Search Results =====\n")


# ------------------------------------------------------
# STEP 5: Ask a query
# ------------------------------------------------------

# invoke() sends the query to retriever.
# Retriever finds most similar documents.

similarity_docs = similarity_retriever.invoke(
    "What is gradient descent?"
)


# ------------------------------------------------------
# STEP 6: Print retrieved documents
# ------------------------------------------------------

for doc in similarity_docs:

    # page_content contains actual text of document
    print(doc.page_content)


# ------------------------------------------------------
# STEP 7: Create MMR Retriever
# ------------------------------------------------------

# MMR = Max Marginal Relevance

# Difference:
# Similarity Search:
# -> Retrieves most similar documents only.

# MMR:
# -> Retrieves relevant AND diverse documents.
# -> Avoids returning duplicate/similar sentences.

mmr_retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}
)


# Print heading
print("\n===== MMR Results =====\n")


# ------------------------------------------------------
# STEP 8: Ask same query using MMR
# ------------------------------------------------------

mmr_docs = mmr_retriever.invoke(
    "What is gradient descent?"
)


# ------------------------------------------------------
# STEP 9: Print MMR retrieved documents
# ------------------------------------------------------

for doc in mmr_docs:
    print(doc.page_content)