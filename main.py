from fastapi import FastAPI, Request  
from typing import Union
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles  
from fastapi.templating import Jinja2Templates  

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "titulo": "Recetas de Cocina",
        "mensaje": "Bienvenido a Recetas de Cocina",
        "descripcion": "Explora nuestras deliciosas recetas para cada ocasión."
    })

@app.get("/entrantes", response_class=HTMLResponse)
async def entrantes(request: Request):
    platos = [
        {"nombre": "Ensalada César", "imagen": "/static/images/ensalada_cesar.jpg"},
        {"nombre": "Gazpacho", "imagen": "/static/images/gazpacho.jpg"},
        {"nombre": "Bruschetta", "imagen": "/static/images/bruschetta.jpg"},
    ]
    return templates.TemplateResponse("entrantes.html", {
        "request": request,
        "titulo": "Recetas: Entrantes",
        "mensaje": "Recetas de Entrantes",
        "descripcion": "Aquí encontrarás recetas ligeras para empezar tu comida.",
        "platos": platos
    })

@app.get("/platos_principales", response_class=HTMLResponse)
async def platos_principales(request: Request):
    platos = [
        {"nombre": "Paella", "imagen": "/static/images/paella.jpg"},
        {"nombre": "Cordero Asado", "imagen": "/static/images/cordero_asado.jpg"},
        {"nombre": "Salmón al Horno", "imagen": "/static/images/salmon_al_horno.jpg"},
    ]
    return templates.TemplateResponse("platos_principales.html", {
        "request": request,
        "titulo": "Recetas: Platos Principales",
        "mensaje": "Recetas de Platos Principales",
        "descripcion": "Encuentra ideas para platos principales deliciosos.",
        "platos": platos
    })

@app.get("/postres", response_class=HTMLResponse)
async def postres(request: Request):
    platos = [
        {"nombre": "Tarta de Queso", "imagen": "/static/images/tarta_queso.jpg"},
        {"nombre": "Flan", "imagen": "/static/images/flan.jpg"},
        {"nombre": "Brownie", "imagen": "/static/images/brownie.jpg"},
    ]
    return templates.TemplateResponse("postres.html", {
        "request": request,
        "titulo": "Recetas: Postres",
        "mensaje": "Recetas de Postres",
        "descripcion": "Descubre dulces irresistibles para cerrar tus comidas.",
        "platos": platos
    })

@app.get("/contacto", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse("contacto.html", {
        "request": request,
        "titulo": "Contacto",
        "mensaje": "Contáctanos",
        "descripcion": "¿Tienes dudas? ¡Escríbenos!"
    })
@app.get("/receta/{plato_id}", response_class=HTMLResponse)
async def receta(request: Request, plato_id: int):
    recetas = {
        1: {
            "nombre": "Ensalada César",
            "imagen": "/static/images/ensalada_cesar.jpg",
            "ingredientes": ["Lechuga", "Crutones", "Queso parmesano", "Aderezo César"],
            "preparacion": "Lava la lechuga y córtala en trozos. Agrega los crutones y el queso parmesano rallado. Aliña con aderezo César y mezcla bien."
        },
        2: {
            "nombre": "Gazpacho",
            "imagen": "/static/images/gazpacho.jpg",
            "ingredientes": ["Tomates", "Pepino", "Pimiento", "Ajo", "Aceite de oliva"],
            "preparacion": "Lava y trocea los tomates, pepino, pimiento y ajo. Licúa con aceite de oliva, sal y un poco de agua fría. Sirve bien frío."
        },
        3: {
            "nombre": "Bruschetta",
            "imagen": "/static/images/bruschetta.jpg",
            "ingredientes": ["Pan", "Tomate", "Albahaca", "Aceite de oliva"],
            "preparacion": "Corta el pan en rebanadas y tuéstalo. Coloca encima tomate picado, albahaca y un chorrito de aceite de oliva."
        },
        4: {
            "nombre": "Paella",
            "imagen": "/static/images/paella.jpg",
            "ingredientes": ["Arroz", "Mariscos", "Azafrán", "Caldo de pescado"],
            "preparacion": "En una paellera, sofríe los mariscos con aceite. Agrega el arroz y el caldo caliente con azafrán. Cocina a fuego lento hasta que el arroz esté en su punto."
        },
        5: {
            "nombre": "Cordero Asado",
            "imagen": "/static/images/cordero_asado.jpg",
            "ingredientes": ["Pierna de cordero", "Ajo", "Romero", "Vino blanco"],
            "preparacion": "Sazona la pierna de cordero con ajo y romero. Hornéala con vino blanco a 180°C por 2 horas, rociándola ocasionalmente con su propio jugo."
        },
        6: {
            "nombre": "Salmón al Horno",
            "imagen": "/static/images/salmon_al_horno.jpg",
            "ingredientes": ["Salmón", "Limón", "Eneldo", "Sal y pimienta"],
            "preparacion": "Coloca el salmón en una bandeja de horno. Añade jugo de limón, eneldo, sal y pimienta. Hornea a 180°C por 20 minutos."
        },
        7: {
            "nombre": "Tarta de Queso",
            "imagen": "/static/images/tarta_queso.jpg",
            "ingredientes": ["Queso crema", "Huevos", "Azúcar", "Galletas", "Mantequilla"],
            "preparacion": "Mezcla queso crema, huevos y azúcar. Coloca sobre una base de galletas con mantequilla y hornea a 160°C por 40 minutos."
        },
        8: {
            "nombre": "Flan",
            "imagen": "/static/images/flan.jpg",
            "ingredientes": ["Leche", "Huevos", "Azúcar", "Caramelo"],
            "preparacion": "Prepara caramelo y viértelo en un molde. Mezcla leche, huevos y azúcar, y agrégalo al molde. Hornea a baño maría a 160°C por 45 minutos."
        },
        9: {
            "nombre": "Brownie",
            "imagen": "/static/images/brownie.jpg",
            "ingredientes": ["Chocolate", "Mantequilla", "Azúcar", "Harina", "Huevos"],
            "preparacion": "Derrite chocolate con mantequilla, mezcla con azúcar y huevos, y agrega harina. Hornea a 180°C por 25 minutos."
        }
    }
    
    plato = recetas.get(plato_id, None)
    if not plato:
        return templates.TemplateResponse("404.html", {"request": request, "mensaje": "Receta no encontrada"})
    
    return templates.TemplateResponse("receta.html", {"request": request, "plato": plato})
