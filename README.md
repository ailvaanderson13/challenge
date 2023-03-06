Como Executar?
# Abra um terminal de sua preferência e siga as instruções abaixo:

# 1 - Crie um ambiente virtual:
```python -m venv venv```
# 2 - Ative o ambiente virtual:

## 2.1 - Se estiver no windows:
##### 2.1.1 - ```cd venv\Script\```
##### 2.1.2 - ```activate```
## 2.2 - Se estiver no linux ou mac:
##### 2.2.1 - ```source venv\bin\activate```


# 3 - Instale as dependencias do projeto:
```pip install -r ./requirements.txt```
# 4 - Execute as migrações:
```python manage.py makemigrations```
```python manage.py migrate```
# 5 - Execute o projeto
```python manage.py runserver```
##### Caso tenha ocorrido tudo certo, aparecerá um endereço como esse em seu terminal: *https://127.0.0.1:8000/*
# 6 - Abra o navegador de sua preferência e acesse o endereço disponibilizado na etapa anterior.
