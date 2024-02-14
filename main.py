from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/contarVocales/{cadena}")
def contarVocales(cadena):
    contador = 0
    for letra in cadena:
        if letra in cadena:
            contador +=1
    return {"Palabra": cadena,"Numero de Vocals":contador, "Numero de letras": len(cadena)}

