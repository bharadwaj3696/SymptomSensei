import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai
from google.genai import types

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

class SymptomRequest(BaseModel):
    symptoms: str

class SymptomResponse(BaseModel):
    response: str

@app.post("/check_symptoms", response_model=SymptomResponse)
async def check_symptoms(request: SymptomRequest):
    try:
        if not request.symptoms or not request.symptoms.strip():
            raise HTTPException(status_code=400, detail="Symptoms field cannot be empty")
        
        prompt = f"""Based on these symptoms: {request.symptoms}, suggest three probable conditions and the recommended next steps for each. IMPORTANT: Start the entire response with a clear educational disclaimer that this is not medical advice and a doctor should be consulted."""
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        if not response.text:
            raise HTTPException(status_code=500, detail="Failed to get response from AI")
        
        return SymptomResponse(response=response.text)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
async def read_root():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
