import sys
import torch
from transformers import pipeline

# You can replace this with any fine-tuned model from HuggingFace Hub
MODEL = "facebook/wav2vec2-base-960h"

def transcribe(audio_path: str) -> str:
    print(f"Loading model: {MODEL}")
    transcriber = pipeline(
        "automatic-speech-recognition",
        model=MODEL,
        device=0 if torch.cuda.is_available() else -1,  # use GPU if available
    )

    print(f"Transcribing: {audio_path}")
    result = transcriber(audio_path)
    return result["text"]


if __name__ == "__main__":
    # Accept audio path as a CLI argument, default to /audio/sample.wav
    audio_file = sys.argv[1] if len(sys.argv) > 1 else "/audio/sample.wav"
    text = transcribe(audio_file)
    print("\n--- Transcription ---")
    print(text)