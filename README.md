# 📸 Image DB Flask

Projeto em Flask para armazenar imagens em **Base64** no **Firebase Firestore**.  
A API possui endpoints completos para CRUD de imagens.

---

## 🚀 Tecnologias

- Python 3.10+  
- Flask  
- Firebase Admin SDK  
- Firestore  

---

## 📂 Estrutura do Projeto

```
image-db-flask/
├── app/
│ ├── controllers/
│ │ └── image_controller.py
│ ├── models/
│ │ └── image_model.py
│ ├── __init__.py
│ └── app.py 
├── serviceAccountKey.json
├── requirements.txt
└── README.md
````

---

## ⚙️ Instalação

1. Clone do repositório
``` bash
git clone https://github.com/seuusuario/image-db-flask.git
cd image-db-flask
```

2. Crie e ative o ambiente virtual Python
``` bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências
``` bash
pip install -r requirements.txt
```

4. Configure o firebase
- Baixe o arquivo `serviceAccountKey.json` do seu projeto Firebase.
- Coloque o arquivo na raiz do projeto (dentro da pasta `image-db-flask`)

---

## ▶️ Rodando o servidor
``` bash
python -m app.app
```

A API estará disponível em:
``` bash
http://127.0.0.1:5000
```
---

## 📚 Endpoints da API

### 1. Criar imagem
`POST /images`

- Tipo de Body: form-data
- Chave: `file` (tipo arquivo)
- A API converte a imagem em Base64 e salva no Firestore.

Exemplo no Postman:
- Key: file
- Value: selecione um arquivo .jpg ou .png

---

### 2. Listar imagens
`GET /images`

Retorna todas as imagens cadastradas.

---

### 3. Obter imagem por ID
`GET /images/<id>`

Retorna os dados da imagem específica.

---

### 4. Atualizar imagem
`PUT /images/<id>`

Permite atualizar a imagem (enviando um novo arquivo).

---

### 5. Deletar imagem
`DELETE /images/<id>`

Deletar a imagem do Firestore. 

---

## 📝 Notas

- As imagens são salvas em Base64 no Firestore.
- O ID é gerado com UUID automaticamente.
- Para segurança, utilize variáveis de ambiente para credenciais em produção.
