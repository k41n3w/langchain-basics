import os
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

def load_api_key():
    """Carrega a chave da API OpenAI a partir das variáveis de ambiente."""
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente 'OPENAI_API_KEY' não foi encontrada.")
    return api_key

def initialize_vector_store(file_path, chunk_size=1000, chunk_overlap=0):
    """Carrega o documento, divide em chunks, gera embeddings e cria o vector store."""
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store

def perform_similarity_search(vector_store, query, k=4):
    """Realiza uma busca de similaridade no vector store com base na consulta."""
    return vector_store.similarity_search(query, k=k)

def main():
    try:
        # Carregar a chave da API
        api_key = load_api_key()

        # Inicializar o vector store
        file_path = './data/state_of_the_union.txt'
        vector_store = initialize_vector_store(file_path)

        # Definir a pergunta e o valor de k
        question = "What did the president say about the John Lewis Voting Rights Act?"
        k = 3  # Número de resultados a serem retornados

        # Realizar a busca de similaridade
        results = perform_similarity_search(vector_store, question, k=k)

        # Exibir os resultados
        print(f"\nPergunta: {question}\n")
        for i, result in enumerate(results, 1):
            print(f"Resultado {i}:\n{result.page_content}\n{'-'*50}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
