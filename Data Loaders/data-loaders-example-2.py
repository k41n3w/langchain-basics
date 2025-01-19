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

class DataProcessor:
    def __init__(self, model):
        self.model = model

    def load_and_ask(self, loader, description, question):
        """Carrega dados e faz uma pergunta usando o contexto carregado."""
        try:
            data = loader.load()
            context = (
                data[0].page_content if hasattr(data[0], "page_content") else str(data[:1])
            )
            messages = ChatPromptTemplate.from_messages(
                [("human", "Answer this {question}, here is some extra {context}")]
            ).format_messages(question=question, context=context)
            response = self.model.invoke(messages)
            print(f"\n----------\nLoaded {description}:\nQuestion: {question}\nResponse: {response.content}\n")
        except Exception as e:
            print(f"Error loading {description}: {e}")

# Initialize processor
processor = DataProcessor(chat_model)

# Examples
processor.load_and_ask(TextLoader("./data/be-good.txt"), "TXT file", "What is the main theme of the text?")
processor.load_and_ask(CSVLoader("./data/Street_Tree_List.csv"), "CSV file", "What are the most common tree types?")
processor.load_and_ask(UnstructuredHTMLLoader("./data/100-startups.html"), "HTML file", "What are the top startups?")
processor.load_and_ask(PyPDFLoader("./data/5pages.pdf"), "PDF file", "Summarize the first page.")
processor.load_and_ask(WikipediaLoader(query="JFK", load_max_docs=1), "Wikipedia page", "What was JFK's full name?")
