import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Load environment variables
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file!")

# Initialize OpenAI model
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

# File path for the text file
file_path = "./data/be-good.txt"

# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Step 1: Load the text file
print("\n----------\n")
print("Loading the TXT file...")
loader = TextLoader(file_path)
loaded_data = loader.load()

print("TXT file successfully loaded!")
print("\n----------\n")

# Step 2: Print the content of the first page
print("Preview of the loaded content (first chunk):")
print(loaded_data[0].page_content)
print("\n----------\n")

# Step 3: Split the text into manageable chunks
print("Splitting the text into chunks...")
text_splitter = CharacterTextSplitter(
    separator="\n\n",         # Use double newlines as separators
    chunk_size=1000,          # Maximum chunk size
    chunk_overlap=200,        # Overlap between chunks
    length_function=len,      # Function to calculate length
    is_separator_regex=False  # Indicates the separator is not a regex
)
texts = text_splitter.create_documents([loaded_data[0].page_content])

# Output chunk statistics
print(f"Number of chunks created: {len(texts)}")
print("\n----------\n")

# Step 4: Print the first chunk of text
print("First chunk of text:")
print(texts[0])
print("\n----------\n")

# Step 5: Create chunks with metadata
print("Creating chunks with metadata...")
metadatas = [{"chunk": idx} for idx in range(len(texts))]
documents = text_splitter.create_documents(
    [loaded_data[0].page_content] * len(metadatas),  # Duplicate content for demonstration
    metadatas=metadatas
)

# Output metadata for the first chunk
print("First chunk with metadata:")
print(documents[0])
print("\n----------\n")
    