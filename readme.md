## What this project is about?
This project is an API which uses hugging face Inference Endpoints and a link of a youtube video to summarize the entire contents of the video based on it's transcripts. The transcripts are fetched via the `youtube_transcript_api` and it is mandatory that the transcripts do exsist for this video.

## How can you run this project locally?
You need
- install docker on you system
- get an API Key from Hugging Face (it's easy trust me :))

Clone this github repo into your system and start by building the docker container, you can do this via
```bash
docker build -t sum-it-up .
```
`sum-it-up` here is the image name, you can have any image name you want.

This would build your container, after which you need to run it. This can be achieved via the command
```bash
docker run -p 8000:8080 <image-name>
```
**Note that the port is 8000 for you local system.** Which means that the url for you will be localhost:8000