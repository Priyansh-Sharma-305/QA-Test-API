# QA/Test Developer Mini Project (FastAPI)

Small REST API + automated tests + CI.

## Endpoints
- GET /health
- GET /users
- POST /users

## Run locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
