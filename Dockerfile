FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg

# Upgrade pip
RUN pip install --upgrade pip

# Install CPU-only PyTorch
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install Whisper and Flask
RUN pip install openai-whisper flask

# Set working directory for runtime
WORKDIR /app

# Run the Flask app (assumes app.py is provided via volume)
CMD ["python", "app.py"]

