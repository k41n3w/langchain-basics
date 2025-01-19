import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

def load_environment_variables():
    """Carrega as variáveis de ambiente necessárias."""
    try:
        load_dotenv(find_dotenv())
        openai_api_key = os.environ["OPENAI_API_KEY"]
        return openai_api_key
    except KeyError:
        raise KeyError("A variável de ambiente 'OPENAI_API_KEY' não foi encontrada.")

def initialize_chat_model(api_key):
    """Inicializa o modelo de chat OpenAI."""
    try:
        chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
        return chat_model
    except Exception as e:
        raise RuntimeError(f"Falha ao inicializar o modelo de chat: {e}")

def load_text_file(file_path):
    """Carrega o conteúdo de um arquivo de texto."""
    try:
        loader = TextLoader(file_path)
        loaded_data = loader.load()
        return loaded_data
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        raise RuntimeError(f"Falha ao carregar o arquivo de texto: {e}")

def split_text(loaded_data, chunk_size=1000, chunk_overlap=200):
    """Divide o texto em pedaços menores."""
    try:
        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        texts = text_splitter.split_documents(loaded_data)
        return texts
    except Exception as e:
        raise RuntimeError(f"Falha ao dividir o texto: {e}")

def main():
    try:
        # Carregar variáveis de ambiente
        openai_api_key = load_environment_variables()
        print("Variáveis de ambiente carregadas com sucesso.")

        # Inicializar o modelo de chat
        chat_model = initialize_chat_model(openai_api_key)
        print("Modelo de chat inicializado com sucesso.")

        # Carregar o arquivo de texto
        file_path = "./data/be-good.txt"
        loaded_data = load_text_file(file_path)
        print(f"Arquivo '{file_path}' carregado com sucesso.")

        # Exibir conteúdo do primeiro documento
        print("\nConteúdo do primeiro documento carregado:\n")
        print(loaded_data[0].page_content)

        # Dividir o texto em pedaços menores
        texts = split_text(loaded_data)
        print(f"\nTexto dividido em {len(texts)} pedaços.")

        # Exibir o conteúdo do primeiro pedaço
        print("\nConteúdo do primeiro pedaço:\n")
        print(texts[0].page_content)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
