import os
from flask import Blueprint, jsonify, render_template
from .pokeneas import get_random_pokenea

bp = Blueprint("main", __name__)

def _container_id():
    # En Docker Swarm tomaremos HOSTNAME, que igual funciona localmente
    return os.getenv("HOSTNAME") or "local-dev"

@bp.get("/info")
def info():
    pk = get_random_pokenea()
    data = {
        "id": pk["id"],
        "nombre": pk["nombre"],
        "altura": pk["altura"],
        "habilidad": pk["habilidad"],
        "container_id": _container_id()
    }
    return jsonify(data)

@bp.get("/filosofia")
def filosofia():
    pk = get_random_pokenea()
    return render_template(
        "filosofia.html",
        nombre=pk["nombre"],
        imagen_url=pk["imagen"],
        frase=pk["frase"],
        container_id=_container_id()
    )
