# Fibonacci-Sequence-API-task
A tiny Flask service that returns the n-th Fibonacci number 
Built with **Python 3.12** and **Flask**, with production-readiness in mind.

---

## Table of Contents
- [Overview](#overview)
- [How to Run Locally](#how-to-run-locally)
- [API Usage](#api-usage)
- [Running Tests](#running-tests)
- [Production Considerations](#production-considerations)

---

## Overview

This API accepts a non-negative integer `n` and returns the nth number in the Fibonacci sequence.  
- **Framework**: Flask
- **Language**: Python 3.12
- **Container-ready**: Yes (via Docker)
- **Testing**: Pytest and Postman

---

## How to Run Locally

1. Clone the repository:
    ```bash
    git clone git@github.com:Jaimewill0511/Fibonacci-Sequence-API-task.git
    cd Fibonacci-Sequence-API-task
    ```

2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate         # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the API:
    ```bash
    python app/main.py
    ```

5. The service will be available at:
    ```
    http://localhost:8000
    ```

---

## API Usage

### 1. Get Fibonacci Number
**Endpoint:**
```bash
GET /fibonacci?n=<integer>
```
**Example:**
```bash
curl "http://localhost:8000/fibonacci?n=10"
```
**Response:**
```bash
{
  "n": 10,
  "fibonacci": 55
}
```
Postman Test
![image](https://github.com/user-attachments/assets/f05c7a3a-b7e5-4319-8a25-44185def02e2)




**Error Handling:**
- Missing n 
- Invalid n (non-integer, negative, or too large)
  
**Example error response:**
```bash
{
  "error": "query param 'n' is required"
}
```
Postman Test
![image](https://github.com/user-attachments/assets/cefdc2bc-2b4d-4ffa-bda2-c4a81345b4f8)


### 2. Health Check
**Endpoint:**
```bash
GET /health
```
**Response:**
```bash
{
  "status": "healthy"
}
```
Postman Test
![image](https://github.com/user-attachments/assets/3683aa0a-089f-4865-afa5-3f0e8d795322)

---
## Running Tests 
Make sure dependencies are installed first.
Then run:
```bash
python -m pytest -q
```
Expected output if all tests pass:
```bash
.....                                                                                                                                                                                                                                                                                                                 [100%]
5 passed in 0.13s
```
---
## Production Considerations
**Containerization**: A Dockerfile can be used to build a lightweight container image(One is found in root folder).
**Example Docker usage**:
```bash
docker build -t fibonacci-api .
docker run -p 8000:8000 fibonacci-api
```
- Used `python:3.12-slim` image for smaller build size
- `.dockerignore` file created to speed up builds and reduce container size by ignoring unnecessary files.

**Deployment**
Ready for deployment with Gunicorn(for concurrency): 
```bash
gunicorn -w 4 -b 0.0.0.0:8000 "main:create_app()"
```
**CI/CD**: GitHub Actions or Azure DevOps pipelines can be configured to automate test runs (`pytest`) and Docker image builds on each push.
    Example:
```yaml
    name: CI Pipeline
    on: [push]
    jobs:
      build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest -q

```


**Monitoring**: Basic logging (`logging.INFO`) is enabled. Can integrate `Prometheus` + `Grafana` and `Loki` for full metrics and logs.

**Scaling**: Stateless API; can be horizontally scaled behind a load balancer (e.g., Azure App Service, Kubernetes HPA).

**Input Validation**: Guardrails (e.g., n <= 92) are in place to prevent abuse(DDOS Attacks) and ensure 64-bit integer safety.

