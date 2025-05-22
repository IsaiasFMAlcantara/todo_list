# TO DO LIST 🛡️📝

Este é um projeto de lista de tarefas desenvolvido com [Streamlit](https://streamlit.io/), [Poetry](https://python-poetry.org/) para gerenciamento de dependências e ambiente virtual, e [SQLite](https://www.sqlite.org/index.html) com [SQLAlchemy](https://www.sqlalchemy.org/) para persistência de dados.

---

## 🚀 Como executar o projeto

### 1. Instalar o `pipx` (caso ainda não tenha)

```bash
pip install pipx
```

### 2. Instalar o Poetry usando `pipx`

```bash
pipx install poetry
```

### 3. Clonar este repositório

Escolha uma das opções abaixo:

* Via HTTPS:

```bash
git clone https://github.com/seu-usuario/todo_list.git
```

* Via SSH:

```bash
git clone git@github.com:seu-usuario/todo_list.git
```

### 4. Acessar o diretório do projeto

```bash
cd todo_list
```

### 5. Instalar as dependências do projeto

```bash
poetry install
```

### 6. Ativar o ambiente virtual

```bash
eval "$(poetry env info --path)/bin/activate"
```

> 💡 Em sistemas Windows, use:
>
> ```powershell
> poetry shell
> ```

### 7. Executar o projeto

```bash
task run
```

---

## 🧰 Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Poetry](https://python-poetry.org/)
* [SQLite](https://www.sqlite.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Taskfile](https://taskfile.dev/) (para automatização de comandos)