# Lightweight Python image keeps container small and fast to download.
FROM python:3.12-slim

# /app is a common working directory name for Python services.
WORKDIR /app

# Install dependencies first to leverage Docker layer caching.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container image.
COPY . ./

# FastAPI listens on port 8000 by default.
EXPOSE 8000

# Run the development server when the container starts.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
