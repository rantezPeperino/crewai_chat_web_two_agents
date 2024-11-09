import sys
from apis import init_api
from crew import ProyectoToolCrew





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apis.init_api:app", host="0.0.0.0", port=8000, reload=True)



