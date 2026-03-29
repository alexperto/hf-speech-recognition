## Build the docker image

```
docker build -t hf-asr .
```

## Run

```
docker run --rm \
  -v $(pwd)/audio:/audio \
  hf-asr \
  python transcribe.py /audio/sample.wav
```