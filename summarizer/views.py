from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from summarizer.services import SummarizerService
from summarizer.dtos import (
    ValidateSummarizeParams,
    ValidateYoutubeSummarizeParams,
    ValidateWikipediaSummarizeParams,
    ValidateNewsArticleSummarizeParams,
)


class SummarizerView(APIView):
    def post(self, request):
        params = ValidateSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "details": ErrorFormat.flat_error_string(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = SummarizerService.bart_summarization(
            params.data["text"], params.data["percentage"]
        )
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )


class YoutubeSummarizerView(APIView):
    def post(self, request):
        params = ValidateYoutubeSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "details": ErrorFormat.flat_error_string(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = SummarizerService.summarize_youtube_transcript(
            params.data["link"], params.data["percentage"]
        )
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )


class WikipediaSummarizerView(APIView):
    def post(self, request):
        params = ValidateWikipediaSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "details": ErrorFormat.flat_error_string(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = SummarizerService.summarize_wikipedia_articles(params.data["query"])
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )


class NewsArticleSummarizerView(APIView):
    def post(self, request):
        params = ValidateNewsArticleSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "details": ErrorFormat.flat_error_string(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = SummarizerService.summarize_news_articles(params.data["link"])
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )
