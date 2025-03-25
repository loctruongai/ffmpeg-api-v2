from fastapi import FastAPI
from kenburns import generate_kenburns
from pydantic import BaseModel

app = FastAPI()

class KenBurnsRequest(BaseModel):
    image_url: str

@app.post("/kenburns")
def create_kenburns(req: KenBurnsRequest):
    return generate_kenburns(req.image_url)
