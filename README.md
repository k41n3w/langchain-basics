
# Langchain Starter Pack (Em construção)

Bem-vindo ao Langchain Starter Pack! Este repositório é um guia prático para quem deseja começar a trabalhar com **Langchain** e suas funcionalidades, oferecendo exemplos claros e explicações detalhadas.

## Sobre as dependências para rodar esse projeto

Amigo se você não consegue instalar o pyenv e o poetry sozinho é melhor voltar uns passos e voltar depois!

## O que é o Langchain?

Langchain é uma poderosa ferramenta para a construção de aplicações baseadas em modelos de linguagem (LLMs). Ele permite que você interaja facilmente com LLMs, realize consultas em grandes volumes de dados, e manipule os resultados para construir soluções avançadas e escaláveis.

## O que você vai encontrar aqui?

Este repositório é um compilado de tutoriais e exemplos práticos que abrangem os principais conceitos e práticas do Langchain. Cada tópico vem com um arquivo Python e uma explicação em markdown para facilitar a compreensão.

### Tópicos abordados:

- **Trabalhando com dados**: Como estruturar, processar e preparar dados para uso com Langchain.
- **Gerenciamento de dependências com Poetry**: Como usar o Poetry para gerenciar as dependências do projeto e garantir que seu ambiente esteja sempre configurado corretamente.
- **Interagindo com LLMs**: Como configurar e usar modelos de linguagem, realizar inferências e interagir com APIs de LLM.
- **Splitters**: Técnicas para dividir textos em chunks menores, facilitando o processamento e a recuperação de informações.
- **Vector Databases**: Como usar bancos de dados vetoriais para armazenar e recuperar dados relacionados a LLMs, otimizando o desempenho das consultas.
- **RAG (Retrieval-Augmented Generation)**: Como utilizar a técnica de RAG para enriquecer as respostas de LLMs com dados externos. Como aprimorar a recuperação de informações em um fluxo de RAG para obter respostas mais precisas e relevantes.

## Como usar

### Pré-requisitos

Antes de começar, você precisará de:

- Python 3.11.4
- Poetry 2.0.1

### Passos iniciais

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/seuusuario/langchain-starter-pack.git
   cd langchain-starter-pack
   ```

2. **Instale as dependências**:

   ```bash
   poetry install
   ```

3. **Rodando os exemplos**:

   Para testar os exemplos, basta rodar os scripts Python diretamente no seu ambiente:

   ```bash
   poetry run python exemplo.py
   ```

4. **Explore os tutoriais**: Cada pasta contém um tutorial específico, com explicações detalhadas em markdown e o código necessário para testar cada conceito.

Se você tiver alguma questão é só me procurar, mas não vai ter porque o conteúdo é impecável.

## Como contribuir

Se você tem sugestões de melhorias, novos exemplos ou encontrou um erro, fique à vontade para abrir uma issue ou um pull request.

## Licença

Este repositório é licenciado sob a [Licença MIT](LICENSE).