from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
async def root(a:int,b:int):
    return {"Result": a+b}