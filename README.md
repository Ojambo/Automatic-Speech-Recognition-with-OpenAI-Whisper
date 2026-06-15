# Automatic Speech Recognition with OpenAI Whisper

A full-stack web application that captures audio from the browser's microphone and transcribes it in real-time using OpenAI's Whisper model. Built as a demonstration of AI-powered speech recognition integrated into a web interface.

## Features

- **Browser-based audio recording** using the Web Audio API and MediaRecorder
- **Automatic speech-to-text transcription** powered by OpenAI Whisper (tiny.en English model)
- **Containerized deployment** with Docker/Podman for easy setup and reproducibility
- **Simple, clean UI** with start/stop controls and live transcription display

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, JavaScript (Web Audio API, Fetch API) |
| **Backend** | Python, Flask |
| **AI/ML** | OpenAI Whisper (tiny.en model) |
| **Containerization** | Docker / Podman |
| **Dependencies** | FFmpeg (audio processing), PyTorch (CPU) |

## How It Works

1. User clicks **Start** to begin recording via the browser's microphone
2. Audio is captured as chunks using the MediaRecorder API
3. On **Stop**, the audio blob is sent via POST to the Flask backend
4. Whisper's `tiny.en` model transcribes the audio
5. The transcription is returned as JSON and displayed on the page

## Quick Start

### Using Podman

```bash
podman-compose up --build
```

### Using Docker

```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`.

## Project Structure

```
automatic-speech-recognition-ai/
├── app.py                  # Flask backend with Whisper integration
├── Dockerfile              # Container definition (Python 3.10 + Whisper + FFmpeg)
├── podman-compose.yml      # Service orchestration
└── templates/
    └── index.html          # Frontend UI with audio recording and transcription display
```

## Notes

- Uses the **tiny.en** Whisper model (English-only, lightweight) for faster inference
- PyTorch is installed in **CPU-only** mode to keep the container lightweight
- Whisper model cache is persisted in a named volume to avoid re-downloading on restart

## Author

**Edward Ojambo**  
[ojambo.com](https://ojambo.com) | [GitHub](https://github.com/ojambo) | [YouTube: ojamboshop](https://www.youtube.com/@ojamboshop)
