import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Arequipeon",
        "altura": 1.25,
        "habilidad": "Dulce Pegajoso",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/arequipeon.png.jpg",
        "frase": "La vida es más suave con un buen arequipe."
    },
    {
        "id": 2,
        "nombre": "Valenchu",
        "altura": 0.90,
        "habilidad": "Sonrisa Curativa",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/camilo.png.jpg",
        "frase": "Una sonrisa sincera puede iluminar hasta el alma más fría."
    },
    {
        "id": 3,
        "nombre": "Eugenion",
        "altura": 1.10,
        "habilidad": "Razonamiento Cósmico",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/Eugenio.png.jpg",
        "frase": "Pensar diferente también es una forma de evolucionar."
    },
    {
        "id": 4,
        "nombre": "Jaimander",
        "altura": 1.45,
        "habilidad": "Llama de la Amistad",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/jaime.png.jpg",
        "frase": "El fuego que compartes nunca se apaga, solo crece."
    },
    {
        "id": 5,
        "nombre": "Montanachu",
        "altura": 0.65,
        "habilidad": "Voltaje Paisa",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/montanachu.png.jpg",
        "frase": "¡Parce, la energía está en el ambiente!"
    },
    {
        "id": 6,
        "nombre": "Ratardo",
        "altura": 0.40,
        "habilidad": "Escapista Supremo",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/rata%2Cpng.jpg",
        "frase": "No todos los caminos rectos llevan a la meta."
    },
    {
        "id": 7,
        "nombre": "Robertox",
        "altura": 1.00,
        "habilidad": "Fuerza de Voluntad",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/roberto.jpg",
        "frase": "La constancia convierte los sueños en logros."
    },
    {
        "id": 8,
        "nombre": "Sofina",
        "altura": 0.80,
        "habilidad": "Brillo Sereno",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/sofia.png.jpg",
        "frase": "La calma también es poder."
    },
    {
        "id": 9,
        "nombre": "Tangozar",
        "altura": 1.30,
        "habilidad": "Ritmo Imparable",
        "imagen": "https://pokeneas-andres.s3.us-east-1.amazonaws.com/images/tangozar.png.jpg",
        "frase": "Quien baila su propia música nunca pierde el paso."
    }
]

def get_random_pokenea():
    return random.choice(POKENEAS)
