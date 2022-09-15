from fastapi import FastAPI;
from sql import Carreras;
import uvicorn
if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")

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
    
