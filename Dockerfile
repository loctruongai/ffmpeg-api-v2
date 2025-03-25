FROM python:3.10-slim

# Cài các gói hệ thống cần thiết
RUN apt-get update && apt-get install -y ffmpeg curl && apt-get clean

# Cài thư viện Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn
COPY app /app
WORKDIR /app

# Chạy FastAPI bằng Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
