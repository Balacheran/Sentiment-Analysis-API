from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from fastapi.security.api_key import APIKeyHeader, APIKey
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from pydantic import BaseModel
import io

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development, change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name="X-API-KEY")
api_keys = {"f01ba15c3bb5e9378364d66a5e3d170d"}  # Replace with your actual API key

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key not in api_keys:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return api_key

analyzer = SentimentIntensityAnalyzer()

class TextData(BaseModel):
    text: str
@app.get("/")
def read_root(api_key: str = Depends(api_key_header)): 
    return {"context":"Sentiment Analysis API"}

@app.post("/analyze")
async def analyze_text(data: TextData, api_key: APIKey = Depends(get_api_key)):
    sentiment_scores = analyzer.polarity_scores(data.text)
    return {"sentiment": sentiment_scores}

@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...), api_key: APIKey = Depends(get_api_key)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    results = []
    for index, row in df.iterrows():
        sentiment_scores = analyzer.polarity_scores(row["text"])
        results.append({
            "id": row["id"],
            "text": row["text"],
            "timestamp": row.get("timestamp", ""),
            "sentiment": sentiment_scores
        })

    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
