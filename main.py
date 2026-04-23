from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import io

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Background Remover Running"}

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    try:
        input_data = await file.read()

        output_data = remove(input_data)

        return StreamingResponse(
            io.BytesIO(output_data),
            media_type="image/png"
        )

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
