FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
RUN playwright install chromium
RUN playwright install-deps

COPY src/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
