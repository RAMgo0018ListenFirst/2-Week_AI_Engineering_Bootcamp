#EXAMPLE(Loading a PDF File)
"""
from langchain_community.document_loaders import PyPDFLoader

# Initialize the loader with the path to your PDF file
data = PyPDFLoader("document loaders/GRU.pdf")

# Load the PDF content into a list of Document objects (usually one per page)
docs = data.load()

# Print the content of the 15th page (index 14)
print(docs[14])
"""



#Example 2(Splitting using TokenTextSplitter)
"""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

# Load the PDF document
data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()

# Initialize the text splitter
splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

# Split the document into chunks
chunks = splitter.split_documents(docs)

# Print the content of the first chunk
print(chunks[0].page_content)
"""



#Example 3(Splitting using RecurvsiveCharacterTextSplitter)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyPDFLoader("document_loaders/GRU.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)
