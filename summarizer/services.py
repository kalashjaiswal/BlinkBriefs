import re
import json
import nltk
import requests
import wikipedia
from newspaper import Article
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi


class SummarizerService:
    @staticmethod
    def get_youtube_transcript(link: str) -> str:
        video_id = link.split("=")[-1]
        subtitle = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        joined_subtitles = " ".join([sub["text"] for sub in subtitle])
        return joined_subtitles

    @staticmethod
    def bart_inference(text: str, percent: int) -> str:
        total_length = len(text.split(" "))
        min_length = (total_length * percent) // 100

        headers = {"Authorization": "Bearer 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"}
        url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

        data = json.dumps(
            {
                "inputs": text,
                "parameters": {
                    "min_length": min_length,
                    "max_length": (min_length + 60),
                    "do_sample": False,
                },
            }
        )

        response = requests.request("POST", url, headers=headers, data=data)
        print(response.content)
        return json.loads(response.content.decode("utf-8"))

    @staticmethod
    def summarize_youtube_transcript(link: str, percent: int) -> str:
        transcript_content = SummarizerService.get_youtube_transcript(link)
        result = SummarizerService.bart_inference(transcript_content, percent)
        return result

    @staticmethod
    def summarize_wikipedia_articles(query: str) -> str:
        return wikipedia.summary(query)

    @staticmethod
    def summarize_news_articles(link: str) -> str:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
