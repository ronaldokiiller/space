Este é um projeto Django (Python). Para rodar ele localmente, siga estes passos:

1. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Instale as dependências:**
   As dependências estão no arquivo chamado `requirements.txt`. basta rodar:
   ```bash
   pip install -r requirements.txt
   ```


3. **Rode as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

5. **Acesse o projeto no navegador:**
   Normalmente em http://127.0.0.1:8000/


Para acessar o painel administrativo do Django (que normalmente fica em /admin) e fazer login como administrador, você precisa criar um superusuário.

Siga este comando no terminal, dentro da pasta do projeto:

```bash
python manage.py createsuperuser
```

Depois, siga as instruções para escolher um nome de usuário, email e senha.  
Assim que criado, você poderá acessar o admin em http://127.0.0.1:8000/admin e fazer login com este usuário.
