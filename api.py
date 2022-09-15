from fastapi import FastAPI;
from sql import Carreras;


app = FastAPI()

Carr = Carreras()


    
@app.get('/data')
def index():
    return 'Hola esta es mi API'
            

@app.get('/Champion')
def index():
    return  Carr.consultacamp()

@app.get('/Anioo')
def index():
    return Carr.consultaAño()

@app.get('/Circuito')
def index():
    return Carr.consultaCircuito()
@app.get('/Puntos')
def index():
    return Carr.consultaMayorPuntos()
    
