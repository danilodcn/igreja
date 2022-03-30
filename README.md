# Site da Igreja Batista Missionária de Açailândia - MA


Todo o site foi escrito em [Django](https://www.djangoproject.com/) (python) usando [Bootstrap](https://getbootstrap.com/).


## Como rodar o projeto

Instale o poetry usando o comando:

``` sh
pip install poetry
```

logo depois instale as dependências:

``` sh
poetry install
```

logo depois instale as dependências:

``` sh
poetry install
```

por fim faça as migrações e suba o servidor:

``` sh
cd igreja
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
