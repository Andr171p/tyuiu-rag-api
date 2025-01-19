FROM python:3.11

WORKDIR /fastapi_service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "src.api_v1.app:app", "--host", "localhost", "--port", "80"]