# Django-Consultant-Otavio
# v1.0

SOBRE O PROJETO
Este projeto é destinado a um teste de vaga. Na qual um usuário administra quais serão os dados a serem enviados para uma api externa de checagam de viabilidade de crédiot financeiro, 
Após isso o próprio sistema cuida de enviar estes dados para checagem, e ao avaliar a resposta da API, ele segue criando o pedido financeiro a partir da checagem prévia.

Neste arquivo irei explicar o projeto, dependências e como inicializa-lo

### 🛠 Tecnologias utilziadas
------------

- [DJANGO](https://www.djangoproject.com/)
- [PYTHON](https://www.python.org/)
- [REACT](https://react.dev/)

### 🎲 Instalação e configuração
------------

Para este projeto voce necessita das seguintes:
* `python` 3.7 a 3.8.x


# para utilizar a API

```bash

    $ cd template/api
# Caso você não tenha o pyenv, utilize o seguinte comando:
    $ python3 -m venv ./venv
# após a criação inicialize com:
    $ source venv/bin/activate
# caso possua pyenv, prossiga com:
    $ mkvirtualenv env
# caso não houverem erros o hambiente virtual ja estará inicializado, caso não:
    $ workon env
# Instalando as dependências:
    $ pip install -r requirements.txt
# Inicializar o banco de dados:
    $ python manage.py migrate
# Rodando os dados pré cadastrados:
    $ python manage.py loaddata */fixtures/*.yaml

# Enfim inicializando o projeto:
    $ python manage.py runserver
```
# para utilizar a interface:

```bash
    $ cd ui
# agora em diante voce pode substituir o npm por yarn em qualquer um dos comandos abaixo:
#instalando as dependências:
    $ npm install
# rodando o projeto
    $ npm run

```

