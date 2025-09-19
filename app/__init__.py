from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore

db = None  # variável global do Firestore

def create_app():
    app = Flask(__name__)

    # Inicializa Firebase
    global db
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Importa e registra blueprints
    from .controllers.image_controller import image_bp
    app.register_blueprint(image_bp, url_prefix='/images')

    return app
