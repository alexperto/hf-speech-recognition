FROM python:3.11-slim

# System dependencies for audio processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY transcribe.py .

# Directory where you'll mount your local audio files
RUN mkdir /audio

CMD ["python", "transcribe.py"]