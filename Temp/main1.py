from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from textblob import TextBlob
import pandas as pd
import io

app = FastAPI()
security = HTTPBasic()

USER_CREDENTIALS = {
    "username": "admin",
    "password": "password123"
}

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USER_CREDENTIALS["username"] or credentials.password != USER_CREDENTIALS["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"}
        )

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

@app.post("/analyze-sentiment/")
def analyze_sentiment(file: UploadFile = File(...), credentials: HTTPBasicCredentials = Depends(authenticate)):
    try:
        content = file.file.read()
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
        
        results = []
        for index, row in df.iterrows():
            analysis = TextBlob(row['text'])
            polarity = analysis.polarity
            sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
            results.append({
                "id": row['id'],
                "text": row['text'],
                "timestamp": row.get('timestamp', None),
                "sentiment": sentiment,
                "polarity": polarity
            })
        
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {e}")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
