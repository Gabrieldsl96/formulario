# Copilot Instructions — Meu Projeto

Projeto Django 6 com Tailwind CSS, Alpine.js e autenticação completa.
Toda geração de código deve seguir rigorosamente os padrões abaixo.

---

## Stack e Versões

- **Python** 3.12+
- **Django** 6.0
- **Frontend**: Tailwind CSS via CDN + Alpine.js 3.14 via CDN
- **Fonte**: Inter (Google Fonts)
- **Banco de dados**: SQLite (dev) / PostgreSQL (produção)
- **Variáveis de ambiente**: `python-dotenv` + arquivo `.env`

---

## Estrutura de Diretórios

```
meu_projeto/            ← raiz do projeto
├── .github/
│   └── copilot-instructions.md
├── .env                ← NÃO commitar
├── .gitignore
├── manage.py
├── requirements.txt
├── README.md
│
├── meu_projeto/        ← configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/          ← templates globais na RAIZ
│   ├── base.html
│   ├── base_dashboard.html
│   └── <nome_app>/
│       └── *.html
│
├── static/             ← estáticos globais na RAIZ
│   ├── css/global.css
│   └── js/global.js
│
├── staticfiles/        ← gerado por collectstatic (não commitar)
│
└── <nome_app>/         ← cada app segue esta estrutura:
    ├── __init__.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    ├── tests.py
    ├── migrations/
    └── static/<nome_app>/
        ├── css/<nome_app>.css
        ├── js/<nome_app>.js
        └── img/
```

---

## Como Criar um Novo App

**SEMPRE** use o comando Django — nunca crie manualmente:

```bash
python manage.py startapp nome_app
```

Após criar, execute obrigatoriamente:

1. **Registrar em `settings.py`**:
   ```python
   INSTALLED_APPS = [
       ...
       'nome_app.apps.NomeAppConfig',
   ]
   ```

2. **Criar estrutura de diretórios** do app:
   ```
   nome_app/static/nome_app/css/nome_app.css
   nome_app/static/nome_app/js/nome_app.js
   nome_app/static/nome_app/img/
   templates/nome_app/
   ```

3. **Criar `urls.py`** com namespace obrigatório:
   ```python
   app_name = 'nome_app'
   urlpatterns = [...]
   ```

4. **Incluir no `meu_projeto/urls.py`**:
   ```python
   path('prefixo/', include('nome_app.urls', namespace='nome_app')),
   ```

5. **Registrar models no `admin.py`**:
   ```python
   from django.contrib import admin
   from .models import MeuModel
   admin.site.register(MeuModel)
   ```

6. **Rodar migrações**:
   ```bash
   python manage.py makemigrations nome_app
   python manage.py migrate
   ```

---

## Padrões de Código

### Views

- **SEMPRE** usar `@login_required` em todas as views (exceto login e reset de senha)
- Usar views baseadas em funções (FBV) como padrão
- Para CRUD complexo, usar CBV com `LoginRequiredMixin`
- Namespaces nos redirects: `redirect('nome_app:nome_view')`

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

@login_required
def minha_view(request):
    context = {'titulo': 'Minha Página'}
    return render(request, 'nome_app/template.html', context)
```

### Forms

- **SEMPRE** usar `forms.py` para todos os formulários
- Estilizar campos diretamente nos widgets com classes Tailwind
- Padrão de estilo para inputs:

```python
from django import forms

class MeuForm(forms.ModelForm):
    class Meta:
        model = MeuModel
        fields = ['campo1', 'campo2']
        widgets = {
            'campo1': forms.TextInput(attrs={
                'class': (
                    'w-full px-4 py-3 rounded-xl border border-gray-300 '
                    'focus:outline-none focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-transparent transition text-gray-900 '
                    'placeholder-gray-400 bg-white text-sm'
                ),
                'placeholder': 'Placeholder aqui',
            }),
        }
```

### Models

- Usar `verbose_name` e `verbose_name_plural` em todo model
- Usar `__str__` em todo model
- Campos de data: sempre `auto_now_add` / `auto_now`
- Registrar **tudo** no `admin.py`

```python
from django.db import models

class MeuModel(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Meu Model'
        verbose_name_plural = 'Meus Models'
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome
```

### URLs

- **SEMPRE** usar `app_name` (namespace) em cada `urls.py`
- Nomes de rotas em snake_case
- Seguir padrão REST para CRUD: `list`, `create`, `detail`, `update`, `delete`

```python
app_name = 'nome_app'

urlpatterns = [
    path('', views.lista, name='list'),
    path('criar/', views.criar, name='create'),
    path('<int:pk>/', views.detalhe, name='detail'),
    path('<int:pk>/editar/', views.editar, name='update'),
    path('<int:pk>/excluir/', views.excluir, name='delete'),
]
```

---

## Padrões de Templates

### Hierarquia de herança

```
base.html                     ← head, meta, CDNs, body wrapper
└── base_dashboard.html       ← sidebar + header + footer (para páginas internas)
    └── nome_app/template.html ← conteúdo específico
```

**Páginas públicas** (login, reset de senha): estendem `base.html`  
**Páginas internas** (protegidas): estendem `base_dashboard.html`

### Template de uma página interna

```html
{% extends 'base_dashboard.html' %}
{% load static %}

{% block title %}Título — Meu Projeto{% endblock %}
{% block page_title %}Título da Página{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'nome_app/css/nome_app.css' %}">
{% endblock %}

{% block content %}
<!-- conteúdo aqui -->
{% endblock %}

{% block extra_js %}
<script src="{% static 'nome_app/js/nome_app.js' %}"></script>
{% endblock %}
```

### Adicionar link no sidebar

No template do app, sobrescreva `{% block sidebar_nav %}`:

```html
{% block sidebar_nav %}
<a href="{% url 'nome_app:list' %}"
   class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium
          text-slate-300 hover:text-white hover:bg-slate-700/60 transition-all duration-200">
    <svg class="flex-shrink-0 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <!-- ícone SVG -->
    </svg>
    <span x-show="open" class="whitespace-nowrap" style="display:none;">Nome do Módulo</span>
</a>
{% endblock %}
```

Para marcar o link como **ativo**, use a block:
```html
{% block nav_nome_app %}text-white bg-indigo-600/20 border border-indigo-500/30{% endblock %}
```

---

## Design System (Tailwind)

### Paleta de cores

| Elemento | Classe |
|---|---|
| Cor primária (botões, foco) | `indigo-600` / `indigo-500` |
| Sidebar background | `slate-900` |
| Sidebar texto | `slate-300` → `white` (hover) |
| Sidebar hover | `slate-700/60` |
| Sidebar ativo | `indigo-600/20` + borda `indigo-500/30` |
| Conteúdo background | `gray-50` |
| Cards | `bg-white rounded-2xl shadow-sm border border-gray-200` |
| Texto principal | `gray-900` |
| Texto secundário | `gray-500` |

### Padrão de cards

```html
<div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
    <!-- conteúdo -->
</div>
```

### Padrão de botões

```html
<!-- Primário -->
<button class="inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2.5 px-5 rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 text-sm shadow-sm">
    Ação
</button>

<!-- Secundário -->
<button class="inline-flex items-center gap-2 bg-white hover:bg-gray-50 text-gray-700 font-medium py-2.5 px-5 rounded-xl border border-gray-300 transition-colors text-sm">
    Cancelar
</button>

<!-- Perigo -->
<button class="inline-flex items-center gap-2 bg-red-600 hover:bg-red-700 text-white font-semibold py-2.5 px-5 rounded-xl transition-colors text-sm">
    Excluir
</button>
```

### Padrão de tabelas

```html
<div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
    <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
            <tr>
                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Coluna</th>
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-100">
            <tr class="hover:bg-gray-50 transition-colors">
                <td class="px-6 py-4 text-sm text-gray-900">Valor</td>
            </tr>
        </tbody>
    </table>
</div>
```

### Padrão de formulários completos

```html
<form method="post" class="space-y-5">
    {% csrf_token %}
    <div>
        <label class="block text-sm font-medium text-gray-700 mb-1.5">Label</label>
        {{ form.campo }}
        {% if form.campo.errors %}
            <p class="mt-1.5 text-xs text-red-600">{{ form.campo.errors.0 }}</p>
        {% endif %}
    </div>
    <div class="flex justify-end gap-3 pt-2">
        <a href="..." class="...botão secundário...">Cancelar</a>
        <button type="submit" class="...botão primário...">Salvar</button>
    </div>
</form>
```

### Mensagens Django

As mensagens são exibidas automaticamente pelo `base_dashboard.html`.
Para acionar nas views:

```python
from django.contrib import messages

messages.success(request, 'Operação realizada com sucesso!')
messages.error(request, 'Ocorreu um erro. Tente novamente.')
messages.warning(request, 'Atenção: verifique os dados.')
messages.info(request, 'Informação importante.')
```

---

## Variáveis de Ambiente

Todas as configurações sensíveis ficam no `.env`. Nunca hardcode no código.

```python
# settings.py — padrão de leitura
import os
from dotenv import load_dotenv
load_dotenv()

MINHA_CONFIG = os.environ.get('MINHA_CONFIG', 'valor_padrao')
```

Sempre adicionar no `.env.example` ao criar uma nova variável:
```env
# Minha nova config
MINHA_CONFIG=valor_exemplo
```

---

## Segurança

- `{% csrf_token %}` obrigatório em todo `<form method="post">`
- Usar `get_object_or_404` ao buscar objetos por PK
- Validar permissões por usuário quando necessário (`request.user`)
- Nunca exibir informações de debug em produção (`DEBUG=False`)
- Usar `messages` para feedback — nunca retornar dados sensíveis no template

---

## Admin Django

Todo model criado deve ser registrado no `admin.py` do respectivo app.
Usar `list_display`, `search_fields` e `list_filter` quando o model tiver mais de 3 campos:

```python
from django.contrib import admin
from .models import MeuModel

@admin.register(MeuModel)
class MeuModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado_em']
    search_fields = ['nome']
    list_filter = ['criado_em']
    ordering = ['-criado_em']
```

---

## Git

### Padrão de commits (Conventional Commits)

```
feat: adiciona módulo de clientes
fix: corrige validação do formulário de login
docs: atualiza README com instruções de deploy
style: ajusta espaçamento nos cards do dashboard
refactor: reorganiza views do app produtos
chore: atualiza requirements.txt
```

### Arquivos que NUNCA devem ser commitados

- `.env`
- `db.sqlite3`
- `staticfiles/`
- `media/`
- `__pycache__/`
- `venv/`

---

## Comandos de Referência

```bash
# Criar novo app
python manage.py startapp nome_app

# Migrações
python manage.py makemigrations nome_app
python manage.py migrate

# Superusuário
python manage.py createsuperuser

# Servidor de desenvolvimento
python manage.py runserver

# Coletar estáticos (produção)
python manage.py collectstatic

# Verificar erros de configuração
python manage.py check

# Atualizar requirements
pip freeze > requirements.txt
```

---

## Rotas Existentes

| URL | Namespace | Descrição |
|---|---|---|
| `/` | `pagina_inicial:index` | Dashboard (protegido) |
| `/accounts/login/` | `accounts:login` | Login |
| `/accounts/logout/` | `accounts:logout` | Logout |
| `/accounts/password-reset/` | `accounts:password_reset` | Recuperação de senha |
| `/admin/` | — | Painel Django Admin |

---

## Apps Existentes

| App | Namespace | Descrição |
|---|---|---|
| `accounts` | `accounts` | Autenticação: login, logout, reset de senha |
| `pagina_inicial` | `pagina_inicial` | Dashboard principal com sidebar |

Ao criar novos módulos, adicionar entrada nesta tabela.
