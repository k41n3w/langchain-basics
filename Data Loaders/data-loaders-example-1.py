import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import (
    TextLoader, CSVLoader, UnstructuredHTMLLoader, PyPDFLoader, WikipediaLoader
)
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file!")

# Initialize OpenAI model
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

def load_and_print(loader, description):
    try:
        data = loader.load()
        print(f"\n----------\nLoaded {description}:\n")
        print(data[:1] if isinstance(data, list) else str(data)[:100])  # Print a preview
    except Exception as e:
        print(f"Error loading {description}: {e}")

# Load files
load_and_print(TextLoader("./data/be-good.txt"), "TXT file")
load_and_print(CSVLoader("./data/Street_Tree_List.csv"), "CSV file")
load_and_print(UnstructuredHTMLLoader("./data/100-startups.html"), "HTML file")
load_and_print(PyPDFLoader("./data/5pages.pdf"), "PDF file")

# Wikipedia example
loader = WikipediaLoader(query="JFK", load_max_docs=1)
wiki_data = loader.load()[0].page_content

# Chat interaction
chat_template = ChatPromptTemplate.from_messages(
    [("human", "Answer this {question}, here is some extra {context}")]
)
messages = chat_template.format_messages(
    question="What was the full name of JFK?",
    context=wiki_data
)
response = chat_model.invoke(messages)
print("\n----------\nResponse from Wikipedia:\n")
print(response.content)
