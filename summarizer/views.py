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
from drf_spectacular.utils import extend_schema


class SummarizerView(APIView):
    @extend_schema(
        description="This API end point can be used to summarize normal text data. It requires a percentage parameter which tells what percent of the total length the summary should be of.",
        request=ValidateSummarizeParams,
        responses=None,
    )
    def post(self, request):
        params = ValidateSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": "Error",
                    "details": params.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = SummarizerService.bart_inference(
            params.data["text"], params.data["percentage"]
        )
        return Response(
            data={"summary": result[0]["summary_text"]},
            status=status.HTTP_200_OK,
        )


class YoutubeSummarizerView(APIView):
    @extend_schema(
        description="This end point is used to summarize transcript of a Youtube Video given a video link.",
        request=ValidateYoutubeSummarizeParams,
        responses=None,
    )
    def post(self, request):
        params = ValidateYoutubeSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": "Error",
                    "details": params.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = SummarizerService.summarize_youtube_transcript(
            params.data["link"], params.data["percentage"]
        )
        return Response(
            data={"summary": result[0]['summary_text']},
            status=status.HTTP_200_OK,
        )


class WikipediaSummarizerView(APIView):
    @extend_schema(
        request=ValidateWikipediaSummarizeParams,
        responses=None,
    )
    def post(self, request):
        params = ValidateWikipediaSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": "Error",
                    "details": params.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = SummarizerService.summarize_wikipedia_articles(params.data["query"])
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )


class NewsArticleSummarizerView(APIView):
    @extend_schema(
            request=ValidateNewsArticleSummarizeParams,
            responses=None,
    )

    def post(self, request):
        params = ValidateNewsArticleSummarizeParams(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": "Error",
                    "details": params.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = SummarizerService.summarize_news_articles(params.data["link"])
        return Response(
            data={"summary": result},
            status=status.HTTP_200_OK,
        )
