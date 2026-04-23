from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Background Remover Running"}

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return StreamingResponse(io.BytesIO(output_data), media_type="image/png")