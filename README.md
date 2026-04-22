# Contractsys

**Sistema web de gerenciamento de contratos de aluguel**, desenvolvido com Python e Flask. Permite cadastrar clientes, registrar contratos com upload de arquivos e visualizar todos os contratos em uma interface web.

---

## Funcionalidades

- Cadastro de contratos com dados do cliente (nome, CPF, e-mail)
- Registro de endereço (local e CEP), valor do aluguel e data de entrada
- Upload de arquivos vinculados ao contrato (PDF, DOCX, DOC)
- Download dos arquivos cadastrados diretamente pelo sistema
- Listagem de todos os contratos armazenados
- Persistência de dados com banco SQLite
- Interface web com Flask e templates Jinja2

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Back-end e lógica da aplicação |
| Flask | Framework web |
| SQLite | Banco de dados local |
| Jinja2 | Templates HTML dinâmicos |
| HTML / CSS | Interface do usuário |
| Git / GitHub | Controle de versão |

---

## Estrutura do projeto

```
Contractsys/
├── app.py           # Rotas e lógica principal da aplicação
├── database.py      # Criação de tabelas e operações com SQLite
├── templates/       # Templates HTML (Jinja2)
├── static/          # Arquivos estáticos (CSS, imagens)
├── uploads/         # Arquivos enviados pelos usuários (gerado automaticamente)
└── README.md
```

---

## Como rodar localmente

**Pré-requisitos:** Python 3.8+ instalado

```bash
# 1. Clone o repositório
git clone https://github.com/felipessantosbsa-cyber/Contractsys.git
cd Contractsys

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3. Instale as dependências
pip install flask

# 4. Rode a aplicação
python app.py
```

Acesse em: **http://127.0.0.1:5000**

---

## Rotas disponíveis

| Rota | Método | Descrição |
|---|---|---|
| `/` | GET | Página inicial |
| `/cadastrar` | GET / POST | Formulário de cadastro de contrato |
| `/listar` | GET | Lista todos os contratos |
| `/status` | GET | Visualização de status dos contratos |
| `/download/<id>` | GET | Download do arquivo vinculado ao contrato |

---

## Modelo de dados

```sql
CREATE TABLE contracts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT    NOT NULL,
    cpf_client  TEXT    NOT NULL,
    location    TEXT    NOT NULL,
    cep         TEXT,
    rent_value  REAL    NOT NULL,
    entry_date  DATE    NOT NULL,
    email       TEXT,
    file_path   TEXT
);
```

---

## Próximas melhorias

- [ ] Autenticação de usuários (login/logout)
- [ ] Status de pagamento por contrato
- [ ] Filtros e busca na listagem
- [ ] Proteção e validação dos dados de entrada

---
