# Formulário — Cadastro de Produtos

Aplicação web desenvolvida com Django 6, Tailwind CSS e Alpine.js para cadastro e gerenciamento de produtos.

---

## Tecnologias

- **Python** 3.12+
- **Django** 6.0
- **Tailwind CSS** via CDN
- **Alpine.js** 3.14 via CDN
- **Fonte:** Inter (Google Fonts)
- **Banco de dados:** SQLite (desenvolvimento)

---

## Funcionalidades

- Autenticação (login e logout)
- Dashboard com contador de produtos
- Cadastro de produtos
- Listagem de produtos em tabela
- Edição de produtos
- Exclusão de produtos com confirmação
- Mensagens de feedback (sucesso, erro, aviso)
- Sidebar recolhível

---

## Estrutura do Projeto

```
formulario/
├── .env                    ← variáveis de ambiente (não commitar)
├── .env.example            ← modelo de variáveis de ambiente
├── .gitignore
├── manage.py
├── requirements.txt
│
├── formulario/             ← configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/               ← autenticação
├── pagina_inicial/         ← dashboard
├── produtos/               ← CRUD de produtos
│
├── templates/              ← templates globais
│   ├── base.html
│   ├── base_dashboard.html
│   ├── accounts/
│   └── produtos/
│
└── static/                 ← arquivos estáticos globais
    ├── css/global.css
    └── js/global.js
```

---

## Instalação e Execução

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd formulario
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

---

## Rotas

| URL | Descrição |
|---|---|
| `/` | Dashboard (requer login) |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/produtos/` | Lista de produtos |
| `/produtos/criar/` | Cadastrar produto |
| `/produtos/<id>/editar/` | Editar produto |
| `/produtos/<id>/excluir/` | Excluir produto |
| `/admin/` | Painel Django Admin |

---

## Apps

| App | Namespace | Descrição |
|---|---|---|
| `accounts` | `accounts` | Login, logout |
| `pagina_inicial` | `pagina_inicial` | Dashboard principal |
| `produtos` | `produtos` | CRUD de produtos |

---

## Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar estáticos (produção)
python manage.py collectstatic

# Verificar erros de configuração
python manage.py check

# Atualizar requirements
pip freeze > requirements.txt
```
