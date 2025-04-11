# Plataforma de Cursos

Este projeto consiste em uma plataforma de cursos, com microsserviços responsáveis pelo cadastro de cursos, alunos e professores. Cada serviço é containerizado com Docker, e pode ser acessado de forma independente, com o cliente consumindo as APIs via chamadas HTTP.

## 🛠️ Tecnologias Utilizadas

- **Python** (para desenvolvimento dos microsserviços)
- **FastAPI** (framework para a criação das APIs)
- **SQLAlchemy** (ORM para comunicação com o banco de dados)
- **Docker** (para containerização)
- **SQLite** (banco de dados)

## 🚀 Como Rodar o Projeto

### 1. Clonando o Repositório

Primeiro, clone o repositório do projeto:

```bash
git clone https://github.com/tarciana23/plataforma_cursos.git
cd plataforma-cursos
```

### 2. Configuração do Ambiente

Certifique-se de que o Docker e o Docker Compose estão instalados no seu sistema. Caso não tenha o Docker, você pode instalar a partir deste link: [Instalar Docker](https://docs.docker.com/get-docker/).

### 3. Subindo os Containers

Para iniciar a aplicação, basta rodar o comando abaixo na raiz do projeto, onde o arquivo `docker-compose.yml` está localizado:

```bash
docker-compose up --build
```

O comando irá construir e iniciar todos os serviços necessários. Cada microsserviço será executado em containers separados, como segue:

- **Curso Service**: Porta `8001`
- **Aluno Service**: Porta `8002`
- **Professor Service**: Porta `8003`

### 4. Acessando as APIs

Após o Docker Compose iniciar os containers, você pode acessar as documentações interativas (Swagger) de cada serviço nas seguintes URLs:

- [Curso Service](http://localhost:8001/docs)
- [Aluno Service](http://localhost:8002/docs)
- [Professor Service](http://localhost:8003/docs)

### 5. Interagindo com a API

Cada serviço tem as seguintes rotas:

#### **Curso Service**:
- **POST /cursos**: Cadastrar um novo curso.
- **GET /cursos**: Listar todos os cursos.

#### **Aluno Service**:
- **POST /alunos**: Cadastrar um novo aluno.
- **GET /alunos**: Listar todos os alunos.

#### **Professor Service**:
- **POST /professores**: Cadastrar um novo professor.
- **GET /professores**: Listar todos os professores.

### 6. Parando os Containers

Quando terminar de usar a plataforma, você pode parar os containers com o seguinte comando:

```bash
docker-compose down
```

Isso irá parar e remover os containers, mas os dados no banco de dados SQLite não serão apagados.

## 💡 Estrutura do Projeto

O projeto é dividido em três microsserviços independentes:

### **Curso Service** (`curso_service/`):
- Gerencia o cadastro de cursos.
- Permite listar e cadastrar cursos nas áreas de Programação, Design e Idiomas.

### **Aluno Service** (`aluno_service/`):
- Gerencia o cadastro de alunos.
- Permite listar e cadastrar alunos.

### **Professor Service** (`professor_service/`):
- Gerencia o cadastro de professores.
- Permite listar e cadastrar professores.

Cada microsserviço é um container independente, com seu próprio banco de dados SQLite.

## 📄 Modelos de Dados

### **Curso**:
- **id** (integer, auto-increment)
- **nome** (string)
- **categoria** (string) — Programação, Design, Idiomas

### **Aluno**:
- **id** (integer, auto-increment)
- **nome** (string)
- **email** (string)
- **data_nascimento** (date)

### **Professor**:
- **id** (integer, auto-increment)
- **nome** (string)
- **especialidade** (string)

## ⚙️ Arquitetura

O sistema é construído sobre uma arquitetura de microsserviços. Cada serviço é responsável por uma funcionalidade específica e pode ser escalado ou atualizado de forma independente. O cliente pode consumir essas APIs de forma assíncrona, fazendo chamadas HTTP.

## 📝 Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para a branch principal (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.
