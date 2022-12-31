import re
import nltk
import sklearn
import wikipedia
import transformers
from newspaper import Article
import youtube_transcript_api
from nltk.corpus import stopwords
from youtube_transcript_api import YouTubeTranscriptApi
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BartTokenizer, BartForConditionalGeneration


class SummarizerService:
    @staticmethod
    def get_youtube_transcript(link: str) -> str:
        video_id = link.split("=")[-1]
        subtitle = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        joined_subtitles = " ".join([sub["text"] for sub in subtitle])
        return joined_subtitles

    @staticmethod
    def bart_summarization(text: str, percent: int) -> str:
        tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

        total_length = len(text.split(" "))
        required_length = (total_length * percent) // 100

        input_tensor = tokenizer.encode(text, return_tensors="pt", truncation=True)
        outputs_tensor = model.generate(
            input_tensor,
            max_length=required_length + 60,
            min_length=required_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )

        result = tokenizer.decode(outputs_tensor[0])
        return result

    @staticmethod
    def summarize_youtube_transcript(link: str, percentage: int) -> str:
        transcript_content = SummarizerService.get_youtube_transcript(link)
        result = SummarizerService.bart_summarization(transcript_content, percentage)
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
