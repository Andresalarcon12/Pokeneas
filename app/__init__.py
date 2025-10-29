import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()  # para futuras variables (S3, AWS); ahora no son obligatorias

    app = Flask(__name__)
    # Configs futuras: app.config["S3_BUCKET"] = os.getenv("S3_BUCKET")

    from .routes import bp
    app.register_blueprint(bp)

    @app.get("/")
    def root():
        return {"ok": True, "msg": "Pokeneas API viva. Rutas: /info, /filosofia"}

    return app
