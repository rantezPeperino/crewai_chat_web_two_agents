# main.py
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from crew import ProyectoToolCrew
from concurrent.futures import Future

app = FastAPI()

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="src/proyecto_tool/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    print(f"Mensaje recibido: {message}")  # Imprimir en terminal
    
    inputs = {
        'topic': data
    }
    futuro  = ProyectoToolCrew().crew().kickoff(inputs=inputs)
    # Espera el resultado del agente
    #resultado = futuro.result()
    print(f"Mensaje recibidofuturo***: {futuro.raw}")  # Imprimir en terminal
    # Imprime el resultado
    #print("Resultado del agente:", resultado)
     # Devolver mensaje invertido
    return JSONResponse({"response": futuro.raw}) 