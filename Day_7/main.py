#EXAMPLE 1(Passing a simple prompt to the model)
"""from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Load environment variables from .env file
load_dotenv()

# Initialize the Mistral AI model
model = ChatMistralAI(model = "mistral-small-2506")

# Invoke the model with a prompt
result = model.invoke("Hello ")

# Print the content of the response
print(result.content)"""




#EXAMPLE 2(Passing text file to the model   )
"""
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

# Load API keys from .env
load_dotenv()

# Load the external document
data = TextLoader("document loaders/notes.txt")
docs = data.load()

# Define the AI's behavior and input structure
template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a AI that summarizes the text"),
        ("human", "{data}")
    ]
)

# Initialize the Mistral model
model = ChatMistralAI(model = "mistral-small-2506")

# Format the prompt by extracting the text content from the first document
prompt = template.format_messages(data = docs[0].page_content)

# Send the formatted prompt to the model
result = model.invoke(prompt)

# Output the summary
print(result.content)
"""

#EXAMPLE 3(Passing PDF to the model)
"""
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PDFlloader
from langchain_core.prompts import ChatPromptTemplate

# Load API keys from .env
load_dotenv()

# Load the external document
data = PyPDFLoader("document_loaders/GRU.pdf")
docs = data.load()

# Define the AI's behavior and input structure
template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a AI that summarizes the text"),
        ("human", "{data}")
    ]
)

# Initialize the Mistral model
model = ChatMistralAI(model = "mistral-small-2506")

# Format the prompt by extracting the text content from the first document
prompt = template.format_messages(data = docs[0].page_content)

# Send the formatted prompt to the model
result = model.invoke(prompt)

# Output the summary
print(result.content)
"""

#EXAMPLE 4(Converting PDF into chunks and passing it to the model)
"""
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# Load PDF
data = PyPDFLoader("document loaders/deeplearning.pdf")
docs = data.load()

# Split large text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

# Create prompt template
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text."),
        ("human", "{data}")
    ]
)

# Initialize Mistral model
model = ChatMistralAI(
    model="mistral-small-2506"
)

# Combine all chunks into one string
text = ""

for chunk in chunks:
    text += chunk.page_content + "\n"

# Format prompt
prompt = template.format_messages(data=text)

# Invoke model
result = model.invoke(prompt)

# Print summary
print(result.content)
"""
from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

llm = ChatMistralAI(model="mistral-small-2506")

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

print("Rag system created")

print("press 0 to exit")

while True:
    query = input("You : ")

    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}")

