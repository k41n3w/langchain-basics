
# Starter Pack LangChain - Trabalhando com Loaders e LLMs

Bem-vindo ao primeiro post da série **Starter Pack do LangChain**! Neste tutorial, você aprenderá como carregar diferentes tipos de dados usando os **document loaders** do LangChain e interagir com modelos de linguagem (LLMs) da OpenAI para responder perguntas baseadas nos dados carregados.

---

## Objetivo

O objetivo deste tutorial é explorar o uso de loaders para carregar arquivos e dados estruturados, e utilizar esses conteúdos como base para consultas a modelos de linguagem, como o **GPT-3.5-turbo**. Veremos como processar arquivos **TXT**, **CSV**, **HTML**, **PDF**, e até mesmo dados da **Wikipedia**, aplicando perguntas dinâmicas para obter respostas úteis.

---

## Pré-requisitos

Antes de começar, certifique-se de que possui o seguinte:

1. **Python** 3.11 ou superior.
2. **Poetry** configurado para gerenciar dependências.
3. Um arquivo `.env` contendo sua chave de API da OpenAI:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

4. As dependências instaladas no seu projeto:
   ```bash
   poetry install
   ```

---

## Estrutura do Código

### 1. Configurando o Ambiente

Carregamos as variáveis de ambiente usando o pacote `dotenv` e inicializamos o modelo OpenAI com a API key armazenada no `.env`:

```python
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file!")

# Initialize OpenAI model
chat_model = ChatOpenAI(model="gpt-3.5-turbo")
```

---

### 2. Criando a Função de Carregamento

A função `load_and_print` é responsável por carregar os dados e exibir uma prévia do conteúdo carregado. Isso nos ajuda a validar o carregamento antes de avançar com os dados:

```python
def load_and_print(loader, description):
    try:
        data = loader.load()
        print(f"\n----------\nLoaded {description}:\n")
        print(data[:1] if isinstance(data, list) else str(data)[:100])  # Print a preview
    except Exception as e:
        print(f"Error loading {description}: {e}")
```

---

### 3. Carregando Diferentes Tipos de Arquivos

Usamos diferentes loaders disponíveis no **LangChain** para carregar e processar arquivos.

#### 3.1 Arquivo TXT

O **TextLoader** é usado para carregar arquivos de texto simples. Neste exemplo, carregamos o arquivo `be-good.txt`:

```python
load_and_print(TextLoader("./data/be-good.txt"), "TXT file")
```

#### 3.2 Arquivo CSV

O **CSVLoader** é utilizado para carregar arquivos no formato CSV. Aqui, processamos o arquivo `Street_Tree_List.csv`:

```python
load_and_print(CSVLoader("./data/Street_Tree_List.csv"), "CSV file")
```

#### 3.3 Página HTML

Para carregar e processar páginas HTML, usamos o **UnstructuredHTMLLoader**. Este exemplo carrega o arquivo `100-startups.html`:

```python
load_and_print(UnstructuredHTMLLoader("./data/100-startups.html"), "HTML file")
```

#### 3.4 Arquivo PDF

Para arquivos PDF, utilizamos o **PyPDFLoader**, que carrega o conteúdo do arquivo e divide as páginas automaticamente:

```python
load_and_print(PyPDFLoader("./data/5pages.pdf"), "PDF file")
```

---

### 4. Consultando Dados da Wikipedia

Além de carregar arquivos, também podemos acessar dados da Wikipedia diretamente com o **WikipediaLoader**. Aqui, carregamos informações sobre o ex-presidente dos EUA, **John F. Kennedy (JFK)**:

```python
loader = WikipediaLoader(query="JFK", load_max_docs=1)
wiki_data = loader.load()[0].page_content
```

---

### 5. Fazendo Perguntas com o LangChain

Com os dados carregados, formatamos uma pergunta e enviamos para o modelo OpenAI. Neste exemplo, perguntamos: **"What was the full name of JFK?"**:

```python
from langchain_core.prompts import ChatPromptTemplate

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
```

---

## Resultado Esperado

O código carregará os arquivos TXT, CSV, HTML e PDF, exibindo uma prévia de cada arquivo no console. Para o exemplo da Wikipedia, você verá uma resposta similar a esta:

```plaintext
---------- 
Response from Wikipedia:

The full name of JFK is John Fitzgerald Kennedy.
```

---

## Conclusão

Neste tutorial, aprendemos a usar os loaders do LangChain para carregar diferentes tipos de dados e integrá-los com modelos OpenAI. Essa abordagem é ideal para construir pipelines de processamento de dados e consultas dinâmicas com base em arquivos ou informações externas.

No próximo post da série, exploraremos como dividir textos em **chunks** e adicionar metadados para otimizar as consultas.

---

Espero que este guia tenha sido útil! Caso tenha dúvidas ou sugestões, deixe nos comentários! 😊