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


# para inicializar a API siga estes 3 trechos de codigos abaixo, cada um deles em uma janela do terminal

# 1 - Rodando o backend e suas dependencias
```bash

    $ cd api
# Caso você não tenha o pyenv, utilize o seguinte comando:
    $ python3 -m venv ./venv
# após a criação inicialize com:
    $ source venv/bin/activate
# caso possua pyenv, prossiga com:
    $ mkvirtualenv env
# caso não houverem erros o hambiente virtual ja estará inicializado, caso não:
    $ workon env
# Caso possua pyenv viertualenvwrapper utilize:
    $ mkvirtualenv env
    $ workon env
# Agora siga: 
# Instalando as dependências:
    $ pip install -r requirements.txt
# Inicializar o banco de dados:
    $ python manage.py migrate
# Rodando os dados pré cadastrados:
    $ python manage.py loaddata */fixtures/*.yaml
```

# 2 - Criando o docker container para o redis ( broker do celery )
```bash

    $ cd redis
# Pra inicializar a instancia do redis ( o broker do celery )
    $ docker compose up
# Após o inicio do redis, o terminal deve estar ocupado, entao para isso abra uma nova janela no terminal e:
# O seu redis deve estar inicializado no docker, mas agora dentro de uma maquina chamada redis,
# Entao neste caso o seguitne coando irá fazer com que o redis funcione corretamente
    $ docker exec -it redis-redis-1 redis-cli
# Caso o container naos esteja rodando dentro de uma maquina especifica, rode o seguinte
    $ docker exec -it redis-1 redis-cli
# Utilize o comando para testar a comunicaçao:
    $ ping
# Caso bem sucedida o retorno sera: 'PONG', e seu servidor redis estará rodando.
```

# 3 - Inicializando o celery
```bash

    $ cd api

# Caso você não tenha o pyenv, utilize o seguinte comando:
    $ python3 -m venv ./venv
# após a criação inicialize com:
    $ source venv/bin/activate
# caso possua pyenv, prossiga com:
    $ mkvirtualenv env
# caso não houverem erros o hambiente virtual ja estará inicializado, caso não:
    $ workon env
# Caso possua pyenv viertualenvwrapper utilize:
    $ mkvirtualenv env
    $ workon env
# Agora siga: 
    $ celery -A api worker -l info
# O trecho resultará em uma listagem de todas as tasks que existem no tasks.py ( uma no caso deste projeto )
# O trecho terá uma mensagem positiva de conexção caso foi feito após a correta inicialização do redis no passo 2 
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

