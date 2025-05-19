import os
from dotenv import load_dotenv
from app import create_app, db
from app.models.usuario_model import Usuario
from flask_bcrypt import Bcrypt

load_dotenv()

app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():
    email = os.getenv("ADMIN_EMAIL")
    nome = os.getenv("ADMIN_NOME")
    senha = os.getenv("ADMIN_SENHA")

    if not all([email, nome, senha]):
        print("Variáveis ADMIN_EMAIL, ADMIN_NOME ou ADMIN_SENHA não definidas no .env")
    elif not Usuario.query.filter_by(email=email).first():
        admin = Usuario(
            nome=nome,
            email=email,
            permissao="admin",
            status=True
        )
        admin.set_senha(senha, bcrypt)
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")
