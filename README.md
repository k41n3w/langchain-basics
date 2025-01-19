
# LangChain Starter Pack

Bem-vindo ao **LangChain Starter Pack**! Este repositório serve como um guia prático para iniciar o desenvolvimento de aplicações utilizando o [LangChain](https://python.langchain.com/), uma biblioteca projetada para facilitar a criação de modelos de linguagem avançados.

## Sumário

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Como Utilizar](#como-utilizar)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Introdução

O LangChain permite a construção de aplicações que combinam modelos de linguagem com fontes de dados externas e pipelines de processamento personalizados. Este repositório fornece exemplos práticos e explicações detalhadas para auxiliar no entendimento e implementação dessas funcionalidades.

## Instalação

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/k41n3w/langchain-basics.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd langchain-basics
   ```

3. **Instale as dependências utilizando o [Poetry](https://python-poetry.org/):**

   ```bash
   poetry install
   ```

   > **Nota:** Certifique-se de que o Poetry está instalado em seu sistema. Para instruções de instalação, consulte a [documentação oficial](https://python-poetry.org/docs/#installation).

4. **Configure as variáveis de ambiente:**

   - Renomeie o arquivo `.env.sample` para `.env`:

     ```bash
     mv .env.sample .env
     ```

   - Edite o arquivo `.env` para incluir suas chaves de API e outras configurações necessárias.

## Estrutura do Projeto

A estrutura do repositório está organizada da seguinte forma:

```plaintext
langchain-basics/
├── data/
│   └── state_of_the_union.txt
├── examples/
│   ├── data_loaders.py
│   ├── embeddings.py
│   ├── rag_with_lcel.py
│   ├── retrievers.py
│   ├── splitters.py
│   ├── top_k.py
│   └── vector_store.py
├── tests/
│   └── test_example.py
├── .env.sample
├── README.md
├── poetry.lock
└── pyproject.toml
```

- **`data/`**: Contém arquivos de dados utilizados nos exemplos.
- **`examples/`**: Inclui scripts demonstrando diferentes funcionalidades do LangChain.
- **`tests/`**: Contém testes para validar o funcionamento dos exemplos.
- **`.env.sample`**: Modelo para configuração de variáveis de ambiente.
- **`README.md`**: Este arquivo de documentação.
- **`poetry.lock`** e **`pyproject.toml`**: Arquivos de configuração do Poetry para gerenciamento de dependências.

## Funcionalidades Principais

Este starter pack cobre os seguintes tópicos:

- **Carregamento de Dados**: Utilização de loaders para importar e processar diferentes formatos de dados.
- **Divisão de Texto**: Uso de splitters para segmentar textos longos em partes menores, facilitando o processamento.
- **Geração de Embeddings**: Criação de representações vetoriais de textos para diversas aplicações.
- **Armazenamento Vetorial**: Implementação de vector stores para armazenamento e recuperação eficiente de embeddings.
- **Recuperação de Informação**: Configuração de retrievers para buscar informações relevantes em grandes volumes de dados.
- **RAG (Retrieval-Augmented Generation)**: Combinação de recuperação de dados com geração de texto para respostas mais informadas.
- **Top K**: Seleção das K melhores respostas ou documentos com base em critérios específicos.

## Como Utilizar

1. **Carregamento de Dados:**

   Utilize os loaders para importar dados de diferentes fontes. Por exemplo, para carregar um arquivo de texto:

   ```python
   from langchain_community.document_loaders import TextLoader

   loader = TextLoader('./data/state_of_the_union.txt')
   documents = loader.load()
   ```

2. **Divisão de Texto:**

   Para dividir um documento em partes menores:

   ```python
   from langchain.text_splitter import CharacterTextSplitter

   text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
   texts = text_splitter.split_documents(documents)
   ```

3. **Geração de Embeddings:**

   Para gerar embeddings dos textos:

   ```python
   from langchain_openai import OpenAIEmbeddings

   embeddings = OpenAIEmbeddings(openai_api_key='sua_chave_api')
   text_embeddings = embeddings.embed_documents([text.page_content for text in texts])
   ```

4. **Armazenamento Vetorial:**

   Para armazenar os embeddings em um vector store:

   ```python
   from langchain_community.vectorstores import Chroma

   vector_store = Chroma.from_documents(texts, embeddings)
   ```

5. **Recuperação de Informação:**

   Para configurar um retriever e buscar informações relevantes:

   ```python
   retriever = vector_store.as_retriever()
   query = "Informações sobre o Ato de Direitos de Voto de John Lewis"
   relevant_docs = retriever.get_relevant_documents(query)
   ```

6. **RAG (Retrieval-Augmented Generation):**

   Para combinar recuperação de dados com geração de texto:

   ```python
   from langchain.chains import LLMChain
   from langchain_openai import OpenAI
   from langchain.prompts import ChatPromptTemplate

   llm = OpenAI(temperature=0, openai_api_key='sua_chave_api')
   prompt_template = ChatPromptTemplate.from_messages(
    [
      ("human", "Contexto: {context} Pergunta: {question} Resposta:")
    ]
   )
   llm_chain = LLMChain(llm=llm, prompt=prompt_template)

   context = "".join([doc.page_content for doc in relevant_docs])
   question = "O que é o Ato de Direitos de Voto de John Lewis?"
   response = llm_chain.run({"context": context, "question": question})
   ```

7. **Top K:**

   Para selecionar os K documentos mais relevantes:

   ```python
   k = 5
   top_k_docs = relevant_docs[:k]
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este repositório.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

Aproveite este starter pack para explorar e desenvolver aplicações poderosas com o LangChain!