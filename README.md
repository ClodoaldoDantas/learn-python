# Aprendendo Python

Projeto com exemplos simples para praticar conceitos básicos de Python.

## Como executar

É necessário ter Python 3 instalado. A partir da pasta do projeto, crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows, use estes comandos para ativar o ambiente:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Com o ambiente virtual ativo, instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Agora, execute um exemplo a partir da pasta do projeto:

```bash
python 01-variables/main.py
```

Substitua `01-variables/main.py` pelo caminho do exemplo que deseja executar. Alguns exemplos pedem dados pelo terminal. Para sair do ambiente virtual ao terminar, execute `deactivate`.
