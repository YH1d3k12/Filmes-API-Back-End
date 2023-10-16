# filmes_api_back_end
Este projeto é um desafio proposto, referente a leitura de indicados e vencedores da categoria **Pior Filme** do _Golden Raspberry Awards_.

Sendo requerido a inserção de conteúdo no banco de dados com a leitura de um arquivo.csv, e, o retorno tratado desses dados.

## 🚀 Endpoints 🚀:
1.  **Listagem de Filmes:**
    - **Método:** GET
    - **URL:** `http://127.0.0.1:5000/movies`
    - **Endpoint:** `/movies`
    - **Descrição:** Retorna a lista completa de filmes, possibilitando uma visão geral dos indicados e vencedores da categoria "Pior Filme" no Golden Raspberry Awards.
      
2. **Listagem de Produtores:**
    - **Método:** GET
    - **URL:** `http://127.0.0.1:5000/movies/producers`
    - **Endpoint:** `/producers`
    - **Descrição:** Retorna a lista de produtores envolvidos nos filmes da categoria "Pior Filme", detalhando cada participação individual do produtor.
    
3. **Análise de Prêmios:**
    - **Método:** GET
    - **URL:** `http://127.0.0.1:5000/movies/awards`
    - **Endpoint:** `/awards`
    - **Descrição:** Retorna os três produtores com o menor intervalo de tempo entre premiações e os três produtores com o maior intervalo de tempo entre premiações.

## 🛠 Guia de Instalação Manual 🛠:

#### 1. Clonagem do Repositório
Abra o terminal e insira um dos comandos na pasta desejada:

###### Clonagem via HTTPS
```
git clone https://github.com/YH1d3k12/filmes_api_back_end.git
```

###### Clonagem via Chave SSH
```
git clone git@github.com:YH1d3k12/filmes_api_back_end.git
```

#### 2. Navegação para o Diretório do Projeto
Utilize o comando `cd filmes_api_back_end` para navegar ao diretorio do projeto e abra-o com sua IDE (Ambiente de Desenvolvimento Integrado).

Para Visual Studio Code (vsCode), digite:
```
code .
```

#### 3. Criação do Ambiente Virtual
Abra o terminal na raiz do ambiente e execute o seguinte comando para criar um ambiente virtual e isolar as dependências do projeto:

```
python -m venv venv
```

#### 4. Inicialização do Ambiente Virtual
Para ativar o ambiente virtual, utilize os seguintes comandos no terminal, de acordo com o sistema operacional:

###### Windows
```
venv\Scripts\activate
```

###### Linux
```
source venv/bin/activate
```

para sair do ambiente virtual digite `deactivate`.

#### 5. Instalação de Dependências
Certifique-se de que o ambiente virtual está ativado e, em seguida, execute o seguinte comando no terminal para instalar as dependências listadas no arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

