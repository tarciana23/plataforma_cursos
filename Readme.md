
# Microsserviços Plataforma de Cursos

Este projeto consiste em uma solução de microsserviços para uma plataforma de cursos, permitindo o cadastro de cursos, alunos e professores. A solução está construída utilizando FastAPI, Docker e contém um cliente simples para consumir os microsserviços.

## Estrutura do Projeto

O projeto é composto pelos seguintes microsserviços:

- **curso-service**: Gerencia os cursos disponíveis na plataforma.
- **aluno-service**: Gerencia os alunos cadastrados na plataforma.
- **professor-service**: Gerencia os professores cadastrados na plataforma.

Cada microsserviço está encapsulado em seu próprio contêiner Docker, permitindo a execução isolada de cada um.

Além disso, um **cliente Python** foi desenvolvido para consumir esses microsserviços, buscando as informações de cursos, alunos e professores.

## Requisitos

- Docker
- Docker Compose
- Python 3.9+ (se quiser rodar o cliente diretamente)

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/tarciana23/plataforma_cursos.git
cd seu-diretorio
```

### 2. Construir e iniciar os contêineres Docker

Com o **Docker Compose**, você pode iniciar todos os microsserviços simultaneamente. Certifique-se de ter o `docker-compose.yml` na raiz do projeto.

```bash
docker-compose up --build
```

Isso vai construir as imagens dos microsserviços e iniciar os contêineres.

### 3. Executar o cliente Python

O cliente Python foi projetado para consumir os microsserviços e mostrar as informações no terminal. Para executá-lo, basta rodar:

```bash
python cliente.py
```

O cliente irá tentar consumir os microsserviços a cada 5 segundos e imprimir os resultados.

### 4. Acessando as APIs

- **Cursos**: `GET http://localhost:8001/cursos`
- **Alunos**: `GET http://localhost:8002/alunos`
- **Professores**: `GET http://localhost:8003/professores`

Essas URLs permitem acessar as informações dos microsserviços, além de possuírem o Swagger (`/docs`) para testes manuais.

### 5. Testando no Swagger

Cada microsserviço possui uma interface Swagger para testes manuais. Você pode acessar o Swagger dos microsserviços nos seguintes links:

- **Curso Service**: [http://localhost:8001/docs](http://localhost:8001/docs)
- **Aluno Service**: [http://localhost:8002/docs](http://localhost:8002/docs)
- **Professor Service**: [http://localhost:8003/docs](http://localhost:8003/docs)

## Endpoints Disponíveis

### Curso Service

- **POST /cursos**: Criar um novo curso.
- **GET /cursos**: Listar todos os cursos ou buscar por categoria (parâmetro `categoria`).

### Aluno Service

- **POST /alunos**: Criar um novo aluno.
- **GET /alunos**: Listar todos os alunos cadastrados.

### Professor Service

- **POST /professores**: Criar um novo professor.
- **GET /professores**: Listar todos os professores cadastrados.

## Estrutura de Diretórios

```
.
├── curso_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── ...
├── aluno_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── ...
├── professor_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── ...
├── cliente.py
├── docker-compose.yml
└── README.md
```

## Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs rápidas e assíncronas.
- **Docker**: Contêineres para isolar e executar os microsserviços.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **SQLite**: Banco de dados simples usado na aplicação.
- **Python**: Linguagem de programação usada para criar o cliente e microsserviços.

## Como Contribuir

1. Faça o fork do repositório.
2. Crie uma branch para sua nova feature (`git checkout -b feature/novafeature`).
3. Commit suas alterações (`git commit -am 'Adicionando nova feature'`).
4. Faça o push para a branch (`git push origin feature/novafeature`).
5. Abra um pull request.

