# Lista de tarefas em Django

Uma aplicação simples em **Django** para uma lista de tarefas.</br>
Neste projeto usei no Frontend o **Bootstrap** para controlar boa parte da responsividade do site,
e na maior parte modifiquei as classes nativas via CSS para personalizar melhor o Framework para este projeto.</br>

**Para esta versão do aplicativo, tive somente que modificar o banco de dados(Originalmente PostreSQL) para o MySQL por causa do local de hospedagem escolhido(PythonAnywhere não dá suporte grátis ao PostgreSQL), uma vez que o Heroku também acabou com a hospedagem gratuita com PostgreSQL.**

###### Para ver esta APP funcionando na internet acesse: Em Breve(mudando o provedor)

<div align="center">
<img height="455" src="https://i.imgur.com/WJgaLV1.png" alt="Tela Index">
<img height="455" src="https://i.imgur.com/8JguufW.png" alt="Tela Tarefas">
</div>

## Este projeto foi feito com:

- [Python 3.10.1](https://www.python.org/)
- [Django 4.0.5](https://www.djangoproject.com/)
- [Bootstrap 5.0](https://getbootstrap.com/)

## Como rodar o projeto?

- Clone esse repositório.
- Crie um virtualenv com Python 3.10.1 no mínimo.
- Ative o virtualenv.
- Instale as dependências listadas em requirements.txt.
- Rode as migrações.
- Configure seu .env(exemplo em .env_config)

git clone https://github.com/fspjonny/lista-de-tarefas.git<br>
cd lista-de-tarefas<br>
python -m venv venv<br>
pip install -r requirements.txt<br>
python manage.py migrate<br>
python manage.py runserver<br>
