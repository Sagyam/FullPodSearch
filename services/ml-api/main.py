from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Processing Service")

class ProcessRequest(BaseModel):
    file_id: str
    config: dict

class ProcessResponse(BaseModel):
    segments: List[dict]
    metadata: dict

@app.post("/api/process", response_model=ProcessResponse)
async def process_audio(request: ProcessRequest):
    try:
        # Processing logic here
        return ProcessResponse(
            segments=[],
            metadata={}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)