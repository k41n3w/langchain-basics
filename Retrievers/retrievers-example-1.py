import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

def load_api_key():
    """Carrega a chave da API OpenAI a partir das variáveis de ambiente."""
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente 'OPENAI_API_KEY' não foi encontrada.")
    return api_key

def initialize_chat_model(api_key, model_name="gpt-3.5-turbo-0125"):
    """Inicializa o modelo de chat OpenAI."""
    return ChatOpenAI(model=model_name, openai_api_key=api_key)

def load_and_split_document(file_path, chunk_size=1000, chunk_overlap=0):
    """Carrega o documento de texto e o divide em pedaços menores."""
    loader = TextLoader(file_path)
    document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(document)

def create_vector_store(documents, embeddings_model):
    """Cria o vector store a partir dos documentos fornecidos."""
    return Chroma.from_documents(documents, embeddings_model)

def retrieve_relevant_documents(vector_store, query):
    """Realiza uma busca de similaridade no vector store com base na consulta."""
    return vector_store.similarity_search(query)

def main():
    try:
        # Carregar a chave da API
        api_key = load_api_key()

        # Inicializar o modelo de chat (não utilizado diretamente neste script, mas instanciado)
        chat_model = initialize_chat_model(api_key)

        # Carregar e dividir o documento
        file_path = './data/state_of_the_union.txt'
        documents = load_and_split_document(file_path)

        # Criar o modelo de embeddings
        embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)

        # Criar o vector store
        vector_store = create_vector_store(documents, embeddings_model)

        # Definir a pergunta
        question = "What did the president say about the John Lewis Voting Rights Act?"

        # Recuperar documentos relevantes
        relevant_docs = retrieve_relevant_documents(vector_store, question)

        # Exibir os resultados
        print("\n----------\n")
        print(f"Pergunta: {question}\n")
        for idx, doc in enumerate(relevant_docs, start=1):
            print(f"Documento {idx}:\n{doc.page_content}\n")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
