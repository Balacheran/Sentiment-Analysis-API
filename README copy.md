# Sentiment-Analysis-API

This repository contains a Sentiment Analysis API built with FastAPI. The API can analyze the sentiment of given text and provides visual insights.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Example Requests and Responses](#example-requests-and-responses)
- [Deployment on Heroku](#deployment-on-heroku)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides an API that analyzes the sentiment of text and returns the sentiment scores. It also includes a frontend built with React for visualizing the sentiment analysis results.

## Features

- Analyze sentiment of text
- Upload CSV files for batch analysis
- Visualize sentiment distribution and trends
- Interactive frontend for manual sentence feeding and file upload

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Pip
- Node.js and npm (for frontend)

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

## API Usage

### GET /

**Description**: Returns a greeting message.

**Request**: 
```bash
curl -X GET http://127.0.0.1:8000/ -H "X-API-KEY: f01ba15c3bb5e9378364d66a5e3d170d"  # Replace with your actual API key
```

**Response**:
```json
{
    "Sentiment-Analysis-API"
}
```

### POST /analyze

**Description**: Analyzes the sentiment of the provided text.

**Request**: 
```bash
curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -H "X-API-KEY: f01ba15c3bb5e9378364d66a5e3d170d" -d '{
    "text": "I love this!"
}'
```

**Response**:
```json
{
    "sentiment": {
        "compound": 0.5,
        "pos": 0.4,
        "neu": 0.6,
        "neg": 0.0
    }
}
```

## Example Requests and Responses

### GET /

**Request**:
```bash
curl -X GET http://127.0.0.1:8000/ -H "X-API-KEY: f01ba15c3bb5e9378364d66a5e3d170d"
```

**Response**:
```json
{
    "Sentiment-Analysis-API"
}
```

### POST /analyze

**Request**:
```bash
curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -H "X-API-KEY: f01ba15c3bb5e9378364d66a5e3d170d" -d '{
    "text": "I love this!"
}'
```

**Response**:
```json
{
    "sentiment": {
        "compound": 0.5,
        "pos": 0.4,
        "neu": 0.6,
        "neg": 0.0
    }
}
```

## Deployment on Heroku

### Steps to Deploy

1. Initialize a Git repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. Create a new Heroku application:
    ```bash
    heroku create your-app-name
    ```

3. Push the code to Heroku:
    ```bash
    git push heroku master
    ```

4. Ensure at least one web dyno is running:
    ```bash
    heroku ps:scale web=1
    ```

Your FastAPI application should now be deployed on Heroku.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
```
