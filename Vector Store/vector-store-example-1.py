import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

def load_environment_variables():
    """Carrega as variáveis de ambiente necessárias."""
    load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")

def load_and_split_document(file_path, chunk_size=1000, chunk_overlap=0):
    """Carrega o documento de texto e divide em chunks."""
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)

def create_vector_store(texts, embeddings, persist_directory="./chroma_store"):
    """Cria o vector store e salva no diretório especificado."""
    try:
        vector_store = Chroma.from_documents(
            texts, embeddings, persist_directory=persist_directory
        )
        return vector_store
    except Exception as e:
        raise RuntimeError(f"Falha ao criar o vector store: {e}")

def main():
    try:
        # Carregar variáveis de ambiente
        openai_api_key = load_environment_variables()
        if not openai_api_key:
            raise ValueError("A variável de ambiente OPENAI_API_KEY não foi encontrada!")

        # Configurar embeddings
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

        # Carregar e dividir documento
        file_path = "./data/state_of_the_union.txt"
        texts = load_and_split_document(file_path)

        # Criar e persistir o vector store
        persist_directory = "./chroma_store"
        vector_store = create_vector_store(texts, embeddings, persist_directory)
        print(f"Vector store criado e salvo em: {persist_directory}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
