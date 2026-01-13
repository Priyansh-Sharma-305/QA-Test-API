[![Tests](https://github.com/Priyansh-Sharma-305/QA-Test-API/actions/workflows/tests.yml/badge.svg)](https://github.com/Priyansh-Sharma-305/QA-Test-API/actions/workflows/tests.yml)


# QA/Test Developer Mini Project (FastAPI)

This project demonstrates a small REST API built with FastAPI, automated API testing using pytest, and a clean project structure suitable for CI/CD workflows.

The goal of this project is to showcase fundamentals relevant to QA/Test Developer roles, including API behavior validation, edge-case testing, and test automation.

---

## Tech Stack

- Python 3.11
- FastAPI
- pytest
- httpx (FastAPI test client dependency)

---

## Project Structure

QA-Test-API/
├── app/
│ ├── init.py
│ └── main.py # FastAPI application
├── tests/
│ └── test_main.py # Automated API tests (pytest)
├── requirements.txt
├── pyproject.toml # pytest configuration
├── README.md
└── .gitignore

---

## API Endpoints

| Method | Endpoint  | Description                |
|-------:|-----------|----------------------------|
| GET    | /health   | Health check endpoint      |
| GET    | /users    | Retrieve all users         |
| POST   | /users    | Create a new user (JSON)   |

---

## Run Locally

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies
pip install -r requirements.txt

3. Start the API server
python -m uvicorn app.main:app --reload

Once running, API documentation is available at:
http://127.0.0.1:8000/docs

Run Automated Tests
All automated tests are located in the tests/ directory.

To execute the test suite:
pytest

Tests validate:
 - API availability and status codes
 - JSON response structure
 - Successful and invalid request handling
 - Basic edge cases

Purpose
This project is intentionally small and focused.
It is designed to demonstrate:
 - REST API fundamentals
 - Automated testing with pytest
 - Clean project organization
 - QA mindset (validation, edge cases, repeatability)

Notes
 - This project uses in-memory data for simplicity.
 - No external database or authentication is included.
 - The emphasis is on correctness, testability, and clarity.

---
