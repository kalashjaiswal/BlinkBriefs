# Sum-It-Up
## What this project is about?
This project is an API which uses hugging face Inference Endpoints and a link of a youtube video to summarize the entire contents of the video based on it's transcripts. The transcripts are fetched via the `youtube_transcript_api` and it is mandatory that the transcripts do exsist for this video.

## How can you run this project locally?
You need
- install docker on you system
- get an API Key from Hugging Face (it's easy trust me :))

Clone this github repo into your system.
Now make a `.env` file in the root directory of this project with the following details
```
DEBUG=False
SECRET_KEY=<any_random_cryptographic_string>
HUGGING_FACE_KEY=<your_hugging_face_key>
```
These are the enviornment variables required to run your project.

First, you'll have to build the docker container which can be done via the command
```bash
docker build -t sum-it-up .
```
`sum-it-up` here is the image name, you can have any image name you want.

This would build your container, after which you need to run it. This can be achieved via the command
```bash
docker run -p 8000:8080 sum-it-up
```
**Note that the port is 8000 for you local system.** Which means that the url for you will be localhost:8000