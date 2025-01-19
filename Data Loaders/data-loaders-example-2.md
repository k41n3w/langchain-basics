
# Starter Pack LangChain - Criando um Processador de Dados com Perguntas Dinâmicas

Neste post da série **Starter Pack do LangChain**, você aprenderá como encapsular a lógica de carregamento de dados e interação com LLMs em uma classe reutilizável. O objetivo é criar um processador que carrega diferentes tipos de dados, formula perguntas e retorna respostas contextuais usando o **GPT-3.5-turbo**.

---

## Objetivo

Criar uma classe para gerenciar o fluxo de trabalho do LangChain, desde o carregamento dos dados até a geração de respostas dinâmicas baseadas nesses dados. Este tutorial cobre:

1. Como carregar arquivos em formatos variados (**TXT**, **CSV**, **HTML**, **PDF**, e **Wikipedia**).
2. Como formular perguntas específicas com base nos dados carregados.
3. Como encapsular a lógica em uma classe reutilizável para facilitar futuras implementações.

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

### 2. Criando a Classe `DataProcessor`

A classe `DataProcessor` encapsula a lógica de carregamento e interação com os dados. Ela inclui o método `load_and_ask`, que:

- Carrega os dados usando o loader fornecido.
- Extrai o conteúdo relevante (como texto ou páginas).
- Formata uma pergunta com o contexto carregado.
- Envia a pergunta para o modelo OpenAI e exibe a resposta.

```python
class DataProcessor:
    def __init__(self, model):
        self.model = model

    def load_and_ask(self, loader, description, question):
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
```

---

### 3. Executando Exemplos

#### 3.1 Arquivo TXT

Carregando e perguntando sobre um arquivo de texto simples:

```python
processor.load_and_ask(TextLoader("./data/be-good.txt"), "TXT file", "What is the main theme of the text?")
```

#### 3.2 Arquivo CSV

Carregando e extraindo informações de um arquivo CSV:

```python
processor.load_and_ask(CSVLoader("./data/Street_Tree_List.csv"), "CSV file", "What are the most common tree types?")
```

#### 3.3 Página HTML

Carregando dados de uma página HTML:

```python
processor.load_and_ask(UnstructuredHTMLLoader("./data/100-startups.html"), "HTML file", "What are the top startups?")
```

#### 3.4 Arquivo PDF

Extraindo informações da primeira página de um PDF:

```python
processor.load_and_ask(PyPDFLoader("./data/5pages.pdf"), "PDF file", "Summarize the first page.")
```

#### 3.5 Dados da Wikipedia

Consultando informações diretamente da Wikipedia:

```python
processor.load_and_ask(WikipediaLoader(query="JFK", load_max_docs=1), "Wikipedia page", "What was JFK's full name?")
```

---

## Resultado Esperado

O código acima processará cada exemplo, exibindo a resposta correspondente no console. Por exemplo, ao perguntar sobre o nome completo de JFK, você verá:

```plaintext
----------
Loaded Wikipedia page:
Question: What was JFK's full name?
Response: The full name of JFK is John Fitzgerald Kennedy.
```

---

## Conclusão

Com a classe `DataProcessor`, encapsulamos a lógica de carregamento e consulta, tornando o código mais modular e reutilizável. Esse padrão pode ser facilmente adaptado para novos tipos de loaders e perguntas mais complexas.

No próximo post da série, exploraremos como dividir documentos extensos em chunks e adicionar metadados para melhorar a recuperação de informações.

---

Espero que este guia tenha sido útil! Caso tenha dúvidas ou sugestões, deixe nos comentários! 😊