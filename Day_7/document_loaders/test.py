#EXAMPLE(Loading a text file)
"""from langchain_community.document_loaders import TextLoader

# Initialize the loader with the path to your text file
loader = TextLoader("document loaders/notes.txt")

# Load the data into a list of Document objects
docs = loader.load()

# Print the loaded documents
print(docs)"""

#Example2
from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator= "",
    chunk_size = 1000,
    chunk_overlap=1
)

data = TextLoader("document loaders/notes.txt")

docs = data.load()

chunks = splitter.split_documents(docs)

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()


