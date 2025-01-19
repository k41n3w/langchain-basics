import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import Document

def load_api_key():
    """Carrega a chave da API OpenAI a partir das variáveis de ambiente."""
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente 'OPENAI_API_KEY' não foi encontrada.")
    return api_key

def initialize_components(api_key):
    """Inicializa os componentes principais do sistema."""
    loader = TextLoader('./data/state_of_the_union.txt')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = Chroma.from_documents(texts, embeddings)
    retriever = vector_store.as_retriever()
    llm = OpenAI(temperature=0, openai_api_key=api_key)
    return llm, retriever

def create_custom_rag_chain(llm, retriever):
    """Cria uma cadeia manual de recuperação e geração."""
    prompt_template = ChatPromptTemplate.from_messages(
        [("human", "Contexto:\n{context}\n\nPergunta: {question}\nResposta:")]
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    
    def retrieve_and_respond(query):
        """Recupera documentos relevantes e gera uma resposta."""
        documents = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in documents])
        response = llm_chain.run({"context": context, "question": query})
        return response, documents

    return retrieve_and_respond

def main():
    try:
        # Carregar a chave da API
        api_key = load_api_key()

        # Inicializar os componentes
        llm, retriever = initialize_components(api_key)

        # Criar a cadeia de recuperação e geração personalizada
        rag_chain = create_custom_rag_chain(llm, retriever)

        # Definir a pergunta
        question = "O que o presidente disse sobre o Ato de Direitos de Voto de John Lewis?"

        # Executar a cadeia RAG
        response, documents = rag_chain(question)

        # Exibir o resultado
        print(f"Pergunta: {question}\n")
        print(f"Resposta: {response}\n")

        # Exibir fontes relevantes
        print("Fontes relevantes:")
        for doc in documents:
            print(f"- {doc.metadata.get('source', 'N/A')}: {doc.page_content[:100]}...")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
