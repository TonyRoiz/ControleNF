# 📄 Controle de Notas Fiscais

Sistema interno web para **gestão de Notas Fiscais recebidas**, com controle de usuários, fornecedores, empresas receptoras e itens da NF. Desenvolvido em **Python Flask**, seguindo boas práticas de Clean Code, arquitetura em camadas (routes, services, repositories) e proteção por autenticação e autorização.

---

## 🚀 Funcionalidades

- Login com autenticação segura (Flask-Login + Bcrypt)
- Controle de sessão com `token_versao` para expiração automática
- Permissões por tipo de usuário (`admin` e `usuario`)
- CRUD de:
  - Usuários (com validações e segurança de último admin)
  - Notas Fiscais
  - Itens da Nota
  - Empresas receptoras
  - Fornecedores
- Proteção contra:
  - Exclusão ou inativação do **último administrador disponível no sistema**
  - CSRF (via Flask-WTF)
  - Redirecionamento malicioso pós-login
- Retorno Flash para usuários

---

## 🛠️ Tecnologias

- **Flask**
- **Flask-WTF** (formulários + CSRF)
- **Flask-Login** (controle de sessão)
- **Flask-Bcrypt** (hash de senhas)
- **Flask-Migrate** (migrations do banco)
- **SQLAlchemy**
- **Jinja2 + Bootstrap 5** (interface moderna e responsiva)

---

## 🧱 Estrutura de Pastas

```

app/
│
├── models/             # Models SQLAlchemy
├── forms/              # Formulários WTForms
├── routes/             # Rotas organizadas por entidade
├── services/           # Lógica de negócio
├── repositories/       # Acesso ao banco
├── templates/          # Templates HTML
├── static/             # CSS customizado
├── decorators/         # Decorador @has\_autorizado
└── init.py         # Criação do app Flask

````

---

## ⚙️ Como executar localmente

1. Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o `.env` com suas variáveis de acordo com o `.env.example`:

4. Execute as migrations:

```bash
flask db upgrade
```

6. Rode a aplicação:

```bash
flask run.py run
```

---

## 👤 Desenvolvido por

**Antônio Rogrigues**
